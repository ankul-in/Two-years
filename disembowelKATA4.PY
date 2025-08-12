#disemvowel a string to hide bad words and sentences . 
def disemvowel(string_):
    x=list(string_)
    for i in x:
        if i.lower()=="a"or"e"or"i"or"o"or"u":
            x.remove(i)
        string_="".join(x)
        
    return string_
print(disemvowel("This website is for losers LOL!"))
