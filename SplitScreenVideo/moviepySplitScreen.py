from moviepy.editor import *

clip_1=VideoFileClip(r"D:\PY\SplitScreenVideo\a1.mov").subclip(0,5)
clip_2=VideoFileClip(r"D:\PY\SplitScreenVideo\a2.mp4").subclip(0,5)
clip_3=VideoFileClip(r"D:\PY\SplitScreenVideo\a3.mp4").subclip(0,5)
clip_4=VideoFileClip(r"D:\PY\SplitScreenVideo\a4.mp4").subclip(0,5)

comb=clips_array([[clip_1,clip_2],[clip_3,clip_4]])
comb.write_videofile(r"D:\PY\SplitScreenVideo\test.mp4")