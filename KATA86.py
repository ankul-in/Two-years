dict={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen",20:"twenty",30:"thirty",40:"forty",50:"fifty",60:"sixty",70:"seventy",80:"eighty",90:"ninety",100:"hundred"}

def wordify(n):
    if n<20:
        return dict[n]
    elif n<100:
        if n%10==0:
            return dict[n]
        else:
            return dict[n//10*10]+ " "+ dict[n % 10]
    elif n<1000:
        if n % 100 ==0:
            return dict[n//100] + " hundred"
        else:
            return dict[n//100]+" hundred "+ wordify(n%100)
    else:
        return "out of range"
# dict = {
#     1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
#     6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
#     11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen",
#     15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
#     19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty",
#     50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
#     90: "ninety", 100: "hundred"
# }

# def wordify(n):
#     if n < 20:
#         return dict[n]
#     elif n < 100:
#         if n % 10 == 0:
#             return dict[n]
#         else:
#             return dict[n // 10 * 10] + " " + dict[n % 10]
#     elif n < 1000:
#         if n % 100 == 0:
#             return dict[n // 100] + " hundred"
#         else:
#             return dict[n // 100] + " hundred " + wordify(n % 100)
#     else:
#         return "Number out of range"

print(wordify(706))