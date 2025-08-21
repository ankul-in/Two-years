#bisect in python
import bisect
sorted_list=[1,3,5,7,9]
new_element=6
insertion_point=bisect.bisect_left(sorted_list,new_element)
sorted_list.insert(insertion_point,new_element)
print("sorted list after insertion ", sorted_list)
print("new element inserted at index", insertion_point)