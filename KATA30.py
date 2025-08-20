def validate_base(num: str, base: int) -> bool:
    validChars=set()
    for i in range(base):
        if i<10:
            validChars.add(str(i))
        if i>=10:
            validChars.add(chr(65+i-10))
    #print(validChars)
    for i in num:
        if i not in validChars:
            return False
    return True
validate_base('7623', 8)
