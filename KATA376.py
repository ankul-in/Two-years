#kata
#https://www.codewars.com/kata/56044de2aa75e28875000017/train/python

def compound_array(a, b):
    answer=[]
    for i in range(max(len(a),len(b))):
        try:
            answer.append(a[i])
        except:
            pass
        try:
            answer.append(b[i])
        except:
            pass
    return answer