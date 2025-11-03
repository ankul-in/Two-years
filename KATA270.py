#kata
#https://www.codewars.com/kata/57873ab5e55533a2890000c7/train/python



def time_correct(time_str):
    if not time_str:
        return time_str  
    try:
        h, m, s = map(int, time_str.split(":"))

        m += s // 60
        s %= 60
        h += m // 60
        m %= 60
        h %= 24
        return f"{h:02}:{m:02}:{s:02}"
    except Exception:
        return None  