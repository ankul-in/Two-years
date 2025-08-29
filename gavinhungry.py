#!/usr/bin/env python
#
# volatile: ALSA / PulseAudio status icon and volume control
# https://github.com/gavinhungry/volatile
#

import alsaaudio
import getopt
import gi
import signal
import sys
import threading

from pulsectl import Pulse, _pulsectl as pulsectl

import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

gi.require_version('Gtk', '3.0')
from gi.repository import GLib, Gtk, Gdk

class Volatile:
  def __init__(self, reverse, maxvol, vicons):
    self.REVERSE_SCROLL = reverse
    self.MAX_VOLUME     = maxvol
    self.VOLATILE_ICONS = vicons

    self.TIMER  = None

    self.PANEL_HEIGHT  = 34  # in pixels, negative if panel is on bottom
    self.SLIDER_WIDTH  = 240 # in pixels
    self.SLIDER_HEIGHT = 30  # in pixels, adjust if the widget doesn't fit
    self.SCROLL_BY     = 2   # increase to scroll "faster"

    self.VOLUME_MULTIPLIER = float(100) / self.MAX_VOLUME

    self.LEVEL_WIDTH   = 200
    self.LEVEL_HEIGHT  = 10
    self.LEVEL_PADDING = 8
    self.LEVEL_TIMEOUT = 2 # seconds
    self.LEVEL_OPACITY = 0.75

    if self.REVERSE_SCROLL:
      self.SCROLL_BY *= -1

    self.init_gtk()
    self.init_pulse()
    self.init_mixer()
    self.init_pulse_watcher()

    self.update(True)
    self.icon.set_visible(True)

    signal.signal(signal.SIGINT, self.quit)
    Gtk.main()

  def quit(self, sig, frame):
    self.pulse.event_listen_stop()
    Gtk.main_quit()

  # create the icon, slider and containing window
  def init_gtk(self):
    self.icon = Gtk.StatusIcon()
    self.icon.connect('activate', self.toggle_slider_window)
    self.icon.connect('popup-menu', self.toggle_mute)
    self.icon.connect('scroll-event', self.on_scroll)

    self.screen = Gdk.Screen.get_default()

    self.slider = Gtk.HScale()
    self.slider.set_can_focus(False)
    self.slider.set_size_request(self.SLIDER_WIDTH, self.SLIDER_HEIGHT)
    self.slider.set_range(0, 100)
    self.slider.set_increments(self.SCROLL_BY, self.SCROLL_BY * 2)
    self.slider.set_draw_value(0)
    self.slider.connect('value-changed', self.on_slide)

    self.slider_window = Gtk.Window()
    self.slider_window.set_skip_taskbar_hint(True)
    self.slider_window.set_skip_pager_hint(True)
    self.slider_window.set_decorated(False)
    self.slider_window.set_resizable(False)
    self.slider_window.set_keep_above(True)
    self.slider_window.set_role('volatile')
    self.slider_window.connect('focus-out-event', self.on_slider_focus_out)

    self.slider_frame = Gtk.Frame()
    self.slider_frame.add(self.slider)
    self.slider_window.add(self.slider_frame)
    self.slider_window.set_accept_focus(False)

    self.level = Gtk.LevelBar()
    self.level.set_can_focus(False)
    self.level.set_size_request(self.LEVEL_WIDTH, self.LEVEL_HEIGHT)
    self.level.set_max_value(100)
    self.level.set_margin_start(self.LEVEL_PADDING)
    self.level.set_margin_end(self.LEVEL_PADDING)
    self.level.set_margin_top(self.LEVEL_PADDING)
    self.level.set_margin_bottom(self.LEVEL_PADDING)

    self.level_window = Gtk.Window()
    self.level_window.set_skip_taskbar_hint(True)
    self.level_window.set_skip_pager_hint(True)
    self.level_window.set_decorated(False)
    self.level_window.set_resizable(False)
    self.level_window.set_keep_above(True)
    self.level_window.set_role('volatile-level')
    self.level_window.stick()

    self.level_frame = Gtk.Frame()
    self.level_frame.add(self.level)
    self.level_window.add(self.level_frame)
    self.level_window.set_accept_focus(False)

    context = self.level_window.get_style_context()
    self.window_bgcolor = context.get_background_color(Gtk.StateFlags.NORMAL)

    if self.LEVEL_OPACITY < 1.0:
      if self.screen.is_composited():
        # http://www.kcjengr.com/programing/2017/11/02/transparent-gtk-window.html
        self.level_window.set_visual(self.screen.get_rgba_visual())
        self.level_window.set_app_paintable(True)
        self.level_window.connect('draw', self.draw_level)
      else:
        self.level_window.set_opacity(self.LEVEL_OPACITY)

    css_provider = Gtk.CssProvider()
    css_provider.load_from_data(b'''
      levelbar > trough {
        padding: 0;
      }

      levelbar > trough > block.filled {
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-right: none;
      }

      levelbar > trough > block.filled.muted {
        background-color: rgba(255, 255, 255, 0.15);
        border: none;
      }
    ''')

    Gtk.StyleContext().add_provider_for_screen(
      self.screen,
      css_provider,
      Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )

  # paint transparent background (supports compositing/blur)
  def draw_level(self, widget, context):
    context.set_source_rgba(
      self.window_bgcolor.red,
      self.window_bgcolor.green,
      self.window_bgcolor.blue,
      self.LEVEL_OPACITY
    )

    context.paint()

  def init_pulse(self):
    self.pulse = Pulse('volatile')
    sink_name = self.pulse.server_info().default_sink_name

    self.sink_description = self.pulse.get_sink_by_name(sink_name).description

  # define mixer and start watch
  def init_mixer(self):
    try:
      self.mixer = alsaaudio.Mixer('Master', device='pulse')
      self.init_pulse()

    except alsaaudio.ALSAAudioError:
      print >> sys.stderr, 'Could not initialize mixer'
      sys.exit(2)

    fd, _eventmask = self.mixer.polldescriptors()[0]
    self.tag = GLib.io_add_watch(fd, GLib.IOCondition.IN, self.watch)

  def reinit_mixer(self):
    GLib.source_remove(self.tag)
    self.init_mixer()

  def on_pulse_event(self, e):
    # e.t._value
    self.reinit_mixer()

  def pulse_watcher(self):
    self.pulse = Pulse('event-printer')
    self.pulse.event_mask_set('module')
    self.pulse.event_callback_set(self.on_pulse_event)
    self.pulse.event_listen()

  def init_pulse_watcher(self):
    self.pulsectl_t = threading.Thread(target=self.pulse_watcher)
    self.pulsectl_t.start()

  #
  def show_slider_window(self):
    if self.slider_window.get_property('visible'):
      return

    self.slider_window.set_position(Gtk.WindowPosition.MOUSE)
    self.slider_window.move(
      self.slider_window.get_position()[0],
      self.PANEL_HEIGHT
    )
    self.slider_window.show_all()
    self.slider_window.present()

  #
  def hide_slider_window(self):
    self.slider_window.hide()

  #
  def toggle_slider_window(self, widget):
    if self.slider_window.get_property('visible'):
      self.hide_slider_window()
    else:
      self.show_slider_window()

  #
  def show_level_window(self):
    if self.level_window.get_property('visible'):
      return

    self.level_window.set_position(Gtk.WindowPosition.CENTER)


    self.level_window.move(
      ((self.screen.get_width() - self.LEVEL_WIDTH) / 2) - self.LEVEL_PADDING,
      1480
    )
    self.level_window.show_all()
    self.level_window.present()

  #
  def show_level_window_with_timeout(self):
    self.show_level_window()

    if self.TIMER != None:
      self.TIMER.cancel()

    self.TIMER = threading.Timer(
      self.LEVEL_TIMEOUT,
      self.hide_level_window
    )

    self.TIMER.start()

  #
  def hide_level_window(self):
    self.level_window.hide()

  #
  def toggle_level_window(self):
    if self.level_window.get_property('visible'):
      self.hide_level_window()
    else:
      self.show_level_window()

  # toggle current mute state
  def toggle_mute(self, widget, button, time):
    mute = not self.mixer.getmute()[0]

    self.mixer.setmute(mute)
    self.update()

  #
  def clamp(self, value, min = 0, max = 100):
    if value > max:
      return max
    if value < min:
      return min

    return int(round(value))

  #
  def level_to_volume(self, level):
    volume = level / self.VOLUME_MULTIPLIER
    return self.clamp(volume, 0, self.MAX_VOLUME)

  #
  def volume_to_level(self, volume):
    level = volume * self.VOLUME_MULTIPLIER
    return self.clamp(level, 0, 100)

  #
  def get_level(self):
    volume = self.mixer.getvolume()[0]
    return self.volume_to_level(volume)

  #
  def set_level(self, level):
    volume = self.level_to_volume(level)
    self.mixer.setvolume(volume)
    self.update()

  # event handler for the HScale being dragged
  def on_slide(self, widget):
    level = widget.get_value()
    self.set_level(level)

  # event handler for scrolling while hovering the icon
  def on_scroll(self, widget, event):
    level = self.get_level()

    if event.direction == Gdk.ScrollDirection.DOWN:
      self.set_level(level - (self.SCROLL_BY))
    elif event.direction == Gdk.ScrollDirection.UP:
      self.set_level(level + (self.SCROLL_BY))

  #
  def on_slider_focus_out(self, widget, event):
    self.hide_slider_window()

  #
  def watch(self, fd, cond):
    self.mixer.handleevents()
    self.update()
    return True

  #
  def set_icon(self, icon_name):
    _icon_name = 'volatile-' + icon_name if self.VOLATILE_ICONS else icon_name
    self.icon.set_from_icon_name(_icon_name)

  # updates the global mixer, moves slider/level and updates icon
  def update(self, no_level = False):
    level = self.get_level()
    muted = self.mixer.getmute()[0]

    self.slider.set_sensitive(not muted)

    if muted:
      self.level.add_offset_value('muted', 100)
    else:
      self.level.remove_offset_value('muted')

    self.slider.set_value(level)
    self.level.set_value(level)

    if not no_level:
      self.show_level_window_with_timeout()

    if muted:
      self.set_icon('audio-volume-muted')
    elif level <= 15:
      self.set_icon('audio-volume-off')
    elif level <= 40:
      self.set_icon('audio-volume-low')
    elif level <= 65:
      self.set_icon('audio-volume-medium')
    else:
      self.set_icon('audio-volume-high')

    tooltip_text = "Volume: {0}%".format(level)

    if muted:
      tooltip_text += ' (muted)'

    if self.sink_description:
      tooltip_text += ' \u2014 {0}'.format(self.sink_description)

    self.icon.set_tooltip_text(tooltip_text)

if __name__ == '__main__':
  try:
    args, _ = getopt.getopt(sys.argv[1:], 'rm:v', [
      'reverse-scroll', 'max-volume=', 'volatile-icons'
    ])
  except getopt.GetoptError as err:
    print >> sys.stderr, err
    sys.exit(1)

  reverse = False
  maxvol = 100
  vicons = False

  for arg, val in args:
    if arg in ('-r', '--reverse-scroll'):
      reverse = True

    if arg in ('-m', '--max-volume'):
      maxvol = min(100, max(0, int(val)))

    if arg in ('-v', '--volatile-icons'):
      vicons = True

  volatile = Volatile(reverse, maxvol, vicons)