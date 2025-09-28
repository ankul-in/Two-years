#https://youtu.be/Ag9uwoT8SxY
from moviepy.editor import *
try:
    video = VideoFileClip(r"videoToGif\fileexample.mp4").subclip(0, 5).rotate(180)
    video.write_gif("D:/PY/videoToGif/test2.gif")
except Exception as e:
    print(f"Error: {e}")