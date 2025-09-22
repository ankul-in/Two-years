#https://youtu.be/4Y7_c6vOnNw

import pywhatkit as pw 
pw.info("Python", lines=3)
text=r"""The Pythonidae, commonly known as pythons, are a family of nonvenomous  snakes found in Africa, Asia, and Australia. Among its members are some of the largest snakes in the world. Ten genera and 39 species are currently recognized."""
pw.text_to_handwriting(text,"myFile.png",[0,0,138])
pw.text_to_handwriting(text)
pw.text_to_handwriting(text,"myFile2.png",[255,0,0])
print("----END---- ")

#INTERNET IS SLOW, extraction of information might take longer time