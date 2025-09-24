#kata
#https://www.codewars.com/kata/53689951c8a5ca91ac000566/train/python
def args_to_string(args):
    string=""
    count=0
    for i in args:
        if count>0:
            string+=" "
        if isinstance(i,list):
            if len(i)==1:
                string+="".join(i)
            else:
                if len(i[0])==1:
                    string+="-"+" ".join(i)
                else:
                    string+="--"+" ".join(i)
        if isinstance(i,str):
            string+=i
        count+=1
        
    return string

print(args_to_string([["f", "bar"], ["baz", "qux"]]))