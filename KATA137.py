#kata
#https://www.codewars.com/kata/5934d648d95386bc8200010b/train/python

def ka_co_ka_de_ka_me(word):
    vowels = "aeiouAEIOU"
    result = ["ka"]
    i = 0
    while i < len(word):
        char = word[i]
        if char in vowels:
            start = i
            while i + 1 < len(word) and word[i + 1] in vowels:
                i += 1
            result.append(word[start:i+1])
            if i < len(word) - 1:
                result.append("ka")
        else:
            result.append(char)
        i += 1

    return "".join(result)

    
      
print(ka_co_ka_de_ka_me("maintenance")) #"kamaikantekanakance"
print(ka_co_ka_de_ka_me("Incomprehensibilities")) #"kaIkancokamprekahekansikabikalikatiekas"