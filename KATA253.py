#kata
#https://www.codewars.com/kata/5ca24526b534ce0018a137b5/train/python

keypad_mapping = {
    '.': '1', ',': '11', '?': '111', '!': '1111',
    'a': '2', 'b': '22', 'c': '222',
    'd': '3', 'e': '33', 'f': '333',
    'g': '4', 'h': '44', 'i': '444',
    'j': '5', 'k': '55', 'l': '555',
    'm': '6', 'n': '66', 'o': '666',
    'p': '7', 'q': '77', 'r': '777', 's': '7777',
    't': '8', 'u': '88', 'v': '888',
    'w': '9', 'x': '99', 'y': '999', 'z': '9999',
    '`': '*', '-': '**', '+': '***', '=': '****',
    ' ': '0'
}
#cant even write simple program what else you gonna write mate
def send_message(message):
    answer=""
    for i in message:
        if i.isupper():
            answer+="#"
            i=i.lower()
        answer+=keypad_mapping[i]
    return answer