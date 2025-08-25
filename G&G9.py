#https://www.geeksforgeeks.org/problems/power-of-numbers-1587115620/1&selectedLang=python3
import math
n=int(input("enter your num-->"))
rev=int(str(n)[::-1])
print(int(math.pow(n,rev)))
