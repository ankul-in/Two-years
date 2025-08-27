#https://www.geeksforgeeks.org/problems/subtraction-in-linked-list/1&selectedLang=python3


class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
def reverse(head):
    prev=None
    while head:
        nxt=head.next
        head.next=prev
        prev=head
        head=nxt
    return prev
def compare(l1,l2):
    len1=len2=0
    a,b=l1,l2
    while a:len1+=1;a=a.next
    while b: len2 +=1;b=b.next
    if len1!=len2:
        return len1>len2
    a,b=l1,l2
    while a and b:
        if a.val != b.val:
            return a.val>b.val
        
        a,b=a.next , b.next
    return True
def subtract(l1,l2):
    l1=reverse(l1)
    l2=reverse(l2)
    dummy=ListNode(0)
    curr=dummy
    borrow=0
    while l1 or l2:
        x=l1.val if l1 else 0
        y=l2.val if l2 else 0
        diff =x-y-borrow
        if diff<0:
            diff+=10
            borrow=1
        else:
            borrow=0
        curr.next=ListNode(diff)
        curr=curr.next
        if l1:l1=l1.next
        if l2:l2=l2.next
    result = reverse (dummy.next)
    while result and result.val ==0 and result.next:
        result = result.next
    return result
def substractLinkedLists(l1,l2):
    if compare(l1,l2):
        return subtract(l1,l2)
    else:
        return subtract(l2,l1)
    
#test case

def createLinkedList(num):
    digit=[int(d) for d in str(num)]
    dummy = ListNode(0)
    curr=dummy
    for d in digit:
        curr.next=ListNode(d)
        curr=curr.next
    return dummy.next
def printLinkedList(head):
    result=[]
    while head:
        result.append(str(head.val))
        head=head.next
    print("->".join(result))
l1=createLinkedList(int(input("enter your first number->")))

l2=createLinkedList(int(input("enter your second number->")))
result=substractLinkedLists(l1,l2)
printLinkedList(result)