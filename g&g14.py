#https://www.geeksforgeeks.org/problems/sort-a-stack/1&selectedLang=python3
def insert_sorted(stack, element):
    if not stack or stack[-1] > element:
        stack.append(element)
    else:
        temp = stack.pop()
        insert_sorted(stack, element)
        stack.append(temp)

def sort_stack(stack):
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        insert_sorted(stack, temp)


stack = [3, 1, 4, 2]
sort_stack(stack)
print(stack)

#get your shit together mate
