#kata
#https://www.codewars.com/kata/565f1bd8f97d3e59c400014a/train/python

def binary_fingers(binary):
    fingers = ["Thumb", "Index", "Middle", "Ring", "Pinkie"]
    if not binary:
        return []
    result = []
    for i in range(len(binary)):
        if binary[len(binary) - 1 - i] == "1":
            result.append(fingers[i])
    return result[::-1]

