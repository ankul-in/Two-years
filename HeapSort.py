# #heap sort
# def heapSort(arr,n,i):
#     #where n is number of elements in list 
   
#     #whee i is largest element in list
#     largest=i
#     #where arr is list
#     a=2*i+1
#     b=2*i+2
#     #define 2 variables to work
#     if a<n and arr[a]>arr[i] :
#         largest=a
#     if b<n and arr[b]>arr[i]:
#         largest=b
#     if largest != i:
#         arr[i],arr[largest]=arr[largest],arr[i]
#     heapSort(arr,n,largest)
# i=9
# arr=[4,5,3,61,7,2,8,1,9]
# n=len(arr)
# heapSort(arr,n,i)

def heapify(arr,n,i):
    largest=i
    a=i*2+1
    b=i*2+2
    if a<n and arr[a]>arr[i]:
        largest=a
    if b<n and arr[b]>arr[i]:
        largest=b
    if largest != i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def heapSort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
arr=[]
n=int(input("enter number of elements in list-->"))
for i in range(n):
    x=int(input("enter number-->"))
    arr.append(x)
heapSort(arr)
print(arr)