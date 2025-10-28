#kata
#https://www.codewars.com/kata/55035eb47451fb61c0000288/train/python
#and i couldnt do this again 
#Ok, Ook, Ooo?  Okk, Ook, Ok?  Okk, Okk, Oo?  Okk, Okk, Oo?  Okk, Okkkk?  Ok, Ooooo?  Ok, Ok, Okkk?  Okk, Okkkk?  Okkk, Ook, O?  Okk, Okk, Oo?  Okk, Ook, Oo?  Ook, Ooook!

def encoder(text):
    def to_okk_format(binary_str):
        # Map each bit to 'O' or 'K'
        return ''.join(['O' if b == '0' else 'K' for b in binary_str])

    encoded_chunks = []
    for char in text:
        binary = format(ord(char), '08b')  # 8-bit binary
        okkified = to_okk_format(binary)
        # Wrap each character's bits in the same style as your decoder expects
        chunk = ', '.join([okkified[i:i+3] for i in range(0, len(okkified), 3)]) + '?'
        encoded_chunks.append(chunk)

    # Join all chunks with the delimiter your decoder splits on
    return 'Ok, Ooooo? '.join(encoded_chunks)
print(encoder(input()))

def converter(s):
    temp=[]
    answer=[]
    for i in s:
        if i in "Oo":
            temp.append("0")
        if i in "Kk":
            temp.append("1")
    x="".join(temp)
    y=[x[i:i+8] for i in range(0,len(x),8)]
    for i in y:
        if len(i)==8:
            dec=int(i,2)
            #print(dec)
            answer.append(chr(dec))
    return "".join(answer)
def okkOokOo(s):
    word=s.split("Ok, Ooooo?")
    answer=[]
    for i in word:
        answer.append(converter(i))
    return " ".join(answer)

print(okkOokOo("OKK, OKO, KK?Ok, Ooooo? OKK, KKO, OK?Ok, Ooooo? OKK, OOO, OK?Ok, Ooooo? OOK, OOO, OO?Ok, Ooooo? OKK, OKO, KK?Ok, Ooooo? OKK, OKO, OO?Ok, Ooooo? OKK, OOO, OK?Ok, Ooooo? OKK, KOO, KO?Ok, Ooooo? OKK, OOO, OK?Ok, Ooooo? OKK, OOO, KO?Ok, Ooooo? OOK, OOO, OO?Ok, Ooooo? OKK, OKO, OO?Ok, Ooooo? OKK, OKK, KK?Ok, Ooooo? OKK, OOK, KK?Ok, Ooooo? OKK, OKK, KK?Ok, Ooooo? OKK, OOO, OK?Ok, Ooooo? OKK, KKO, OK?Ok, Ooooo? OKK, OOO, OK?Ok, Ooooo? OOK, OOO, OO?Ok, Ooooo? OKK, OOO, KK?Ok, Ooooo? OKK, KOK, KO?Ok, Ooooo? OOK, OOO, OO?Ok, Ooooo? OKK, OKK, OK?Ok, Ooooo? OKK, OOO, OK?Ok, Ooooo? OKK, OKO, OK?"))
# print(okkOokOo('Ok, Ook, Okk? Okk, Ok, Ook? Okk, Okkk, O? Okk, Ookkk? Ok, Ookkk? Okkk, Ookk? Ok, Ooooo? Ok, Ok, Ook, O? Okk, Ooook? Okkk, Ok, Oo!'))


