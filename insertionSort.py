#insertion sort
def insertionSort(a):
    for i in range(1,len(a)):
        b=a[i]
        j=i-1
        while j>0 and b<a[j]:
            a[j],a[j+1]=a[j+1],a[j]
            j=j-1
    print(a)
a=[]
n=int(input("enter number of elements in list-->"))
for i in range(n):
    x=int(input("enter number-->"))
    a.append(x)
insertionSort(a)
