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


    def MergeLists(self,headA,headB):
        if headA is None and headB is None:
            return None
        if headA is None and headB is not None:
            return headB
        if headA is not None and headB is None :
            return headA
        if headA.data<=headB.data:
            headA.next=self.MergeLists(headA.next,headB)
        elif headA.data>headB.data:
            temp=headB
            headB=headB.next
            temp.next=headA
            headA=temp
            headA.next=self.MergeLists(headA.next,headB)
        return headA



ll=Linked_list()
head_new=ll.inserNth(3,0)
head_new=ll.inserNth(4,1)
head_new=ll.inserNth(5,2)
print("llinked list 1")
ll.display(head_new)

lt=Linked_list()
head_new1=lt.inserNth(1,0)
head_new1=lt.inserNth(2,1)
head_new1=lt.inserNth(6,2)
print("llinked list 2")
lt.display(head_new1)


merge_head=ll.MergeLists(head_new,head_new1)
print("merged list :")
ll.display(merge_head)



