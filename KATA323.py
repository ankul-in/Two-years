#kata
#https://www.codewars.com/kata/582c297e56373f0426000098/train/python

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def stringify(node):
    if node is None:
        return "None"
    return f"{node.data} -> {stringify(node.next)}"

