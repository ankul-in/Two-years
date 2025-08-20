class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
    def append(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode

    def __str__(self):
        tempNode=self.head
        result=""
        while tempNode is not None:
            result+=str(tempNode.value)
            if tempNode.next is not None:
                result+="-->"
            tempNode=tempNode.next
        return result
    
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
print(new_linked_list)