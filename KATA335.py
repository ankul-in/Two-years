#kata
#https://www.codewars.com/kata/55befc42bfe4d13ab1000007/train/python

class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(head, index):
    current = head
    count = 0
    while current:
        if count == index:
            return current
        count += 1
        current = current.next
    raise IndexError("Index out of range")