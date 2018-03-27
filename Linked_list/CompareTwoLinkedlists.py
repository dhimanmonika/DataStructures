class Node(object):
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next=next_node

class Linked_list:

    def __init__(self):
        self.head=None

    def inserNth(self,data,position):
        if position==0:
            if self.head is None:
                self.head=Node(data)
            else:
                prev=self.head
                self.head=Node(data,prev)
        else:
            nxt=self.head
            for i in range(position):
                prev=nxt
                nxt=nxt.next
            cur=Node(data,nxt)
            prev.next=cur
        return self.head

    def display(self,head):
        if head:
            print(head.data)
            self.display(head.next)


    def CompareTwoLists(self,headA,headB):
        while True:
            if headA is None and headB is None :
                return 1
            if headA is None or headB is None or headA.data !=headB.data:
                return 0
            headA=headA.next
            headB=headB.next





ll=Linked_list()
head_new=ll.inserNth(3,0)
head_new=ll.inserNth(4,0)
head_new=ll.inserNth(5,1)
print("llinked list 1")
ll.display(head_new)

lt=Linked_list()
head_new1=lt.inserNth(3,0)
head_new1=lt.inserNth(4,0)
head_new1=lt.inserNth(5,1)
print("llinked list 2")
lt.display(head_new1)

if lt.CompareTwoLists(head_new,head_new1):
    print("Both linked list are equal")
else:
    print("Linked list are not equal")




