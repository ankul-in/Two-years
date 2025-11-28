#kata
#https://www.codewars.com/kata/55b1fd84a24ad00b32000075/train/python

def afraid(day: str, num: int) -> bool:
    day = day.lower()  
    
    if day == "monday":
        return num == 12
    elif day == "tuesday":
        return num > 95
    elif day == "wednesday":
        return num == 34
    elif day == "thursday":
        return num == 0
    elif day == "friday":
        return num % 2 == 0
    elif day == "saturday":
        return num == 56
    elif day == "sunday":
        return num in (666, -666)
    else:
        raise ValueError("Invalid day of the week")

