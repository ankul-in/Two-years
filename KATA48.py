#kata
#https://www.codewars.com/kata/5977ef1f945d45158d00011f/train/python
def sep_str(st): 
    ans=[]
    words=st.split()
    if not words:
        return []
    maxlength=max(len(word) for word in words)
    i=0
    while i<maxlength:  
        row=[]
        for word in words:
            if i<len(word):
                row.append(word[i])
            else:
                row.append("")
        ans.append(row)
        i+=1
    return ans
    
    


sep_str("Just Live Life Man")