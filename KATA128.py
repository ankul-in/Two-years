#kata
#https://www.codewars.com/kata/587a75dbcaf9670c32000292/train/python

st="HelLO   TherE   My"
#print(st.lower())
def filter_words(st):
    st = st.strip()
    st = " ".join(st.split())
    return st[0].upper() + st[1:].lower() if st else ''
print(filter_words(st))