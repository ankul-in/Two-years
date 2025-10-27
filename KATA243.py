#kata
#https://www.codewars.com/kata/57cf3dad05c186ba22000348/train/python

def decode_resistor_colors(bands):
    colorCode={"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9}
    x=bands.split()
    stringreturn = int(str(colorCode[x[0]])+str(colorCode[x[1]])) 
    return stringreturn
print(decode_resistor_colors("brown black black"))