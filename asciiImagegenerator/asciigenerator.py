import pywhatkit as kit

kit.image_to_ascii_art(r"D:\PY\asciiImagegenerator\Screenshot 2025-08-17 051432.png","ascii.txt")


import ascii_magic
output = ascii_magic.from_image_file(r"D:\PY\asciiImagegenerator\Screenshot 2025-08-17 051432.png",chars="#",column=300)

ascii_magic.to_terminal(output)