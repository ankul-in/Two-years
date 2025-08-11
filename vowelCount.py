def get_count(sentence):
    x=list(sentence)
    print(x)
    count=0
    for i in x:
        if i.lower()=="a"or"e"or"i"or"o"or"u":
            count+=1  
    return count
print(get_count("abracadabra"))