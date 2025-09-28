#https://youtu.be/KNUcpLBd5Wg

from moviepy.editor import *

clip = VideoFileClip(r"D:\PY\watermark\test.mp4").subclip(0,5)
txt_clip=TextClip("This is a WaterMark",fontsize=50,color="Black")
txt_clip = txt_clip.set_position("Top").set_duration(5)

video=CompositeVideoClip([clip,txt_clip])

video.write_videofile("test7.mp4")
