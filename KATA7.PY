#kata 7 number of people in bus
def number(arr):
    # Good Luck!
    input=0
    output=0
    for i in arr:
        input=input+int(i[0])
        output=output+int(i[1])
    return input-output