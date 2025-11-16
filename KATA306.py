#kata
#https://www.codewars.com/kata/5937ae46377144bb2f000029/train/python

def get_rectangle_string(width, height):
    rectangle = ""
    rectangle += "*" * width + "\r\n"
    for _ in range(height - 2):
        rectangle += "*" + " " * (width - 2) + "*" + "\r\n"
    rectangle += "*" * width + "\r\n"
    return rectangle