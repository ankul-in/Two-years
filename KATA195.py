# #kata
# #https://www.codewars.com/kata/542f0c36d002f8cd8a0005e5/train/python


def last_chair(n):
    
    return n-1
print(last_chair(17))
def farthest_empty_index(arr):
    occupied = [i for i, val in enumerate(arr) if val is not None]
    empty = [i for i, val in enumerate(arr) if val is None]
    if not empty or not occupied:
        return 0 
    max_distance = -1
    best_index = None
    for e in empty:
        min_dist = min(abs(e - o) for o in occupied)
        if min_dist > max_distance:
            max_distance = min_dist
            best_index = e
    return best_index

def last_chair(n):
    arr=[None]*n
    chairs=[i for i in range(1,n+1)]
    for i in chairs:
        x=farthest_empty_index(arr)
        arr[x]=i
        print(arr,end="\n")
    return arr.index(n)
print(last_chair(15))


# # # def quick_sort(arr):
# # #     if len(arr) <= 1:  # Base case: arrays with 0 or 1 element are already sorted
# # #         return arr
# # #     else:
# # #         pivot = arr[0]  # Choosing the first element as the pivot
# # #         less_than_pivot = [x for x in arr[1:] if x <= pivot]  # Elements less than or equal to pivot
# # #         greater_than_pivot = [x for x in arr[1:] if x > pivot]  # Elements greater than pivot
# # #         return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# # # # Example usage
# # # arr = [10, 7, 8, 9, 1, 5]
# # # sorted_arr = quick_sort(arr)


# # # def insertion_sort1(arr):
# # #     for i in range(1, len(arr)):
# # #         print(i)
# # #         key = arr[i]
# # #         j = i - 1
# # #         while j >= 0 and key < arr[j]:
# # #             arr[j + 1] = arr[j]
# # #             j -= 1
# # #         arr[j + 1] = key
# # # print(insertion_sort1([1,2,3,4,5,6,7,8,9,10]))
# # # def rev_insertion_sort(arr):
# # #     for i in range(1,len(arr))[::-1]:
# # #         print(i)
# # #         key = arr[i]
# # #         j = i - 1
# # #         while j <= len(arr) and key > arr[j]:
# # #             arr[j ] = arr[j-1]
# # #             j -= 1
# # #         arr[j - 1] = key
# # #     return arr
# # # print(rev_insertion_sort([1,2,3,4,5,6,7,8,9,10]))
# # def rev_insertion_sort(arr):
# #     for i in range(1, len(arr)):
# #         key = arr[i]
# #         j = i - 1
# #         while j >= 0 and arr[j] < key:
# #             arr[j + 1] = arr[j]
# #             j -= 1
# #         arr[j + 1] = key
# #     return arr

# # print(rev_insertion_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# def last_chair(n):
#     arr=[i for i in range(1,n+1)]
#     for i in range(1,len(arr))[::-1]:
#         print(i)
#         key = arr[i]
#         j = i - 1
#         while j <= len(arr) and key > arr[j]:
#             arr[j ] = arr[j-1]
#             j -= 1
#         arr[j - 1] = key
#     return arr
    
    
#     return arr


# print(last_chair(10))




