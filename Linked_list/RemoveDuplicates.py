"""remove duplicates from sorted linked list"""


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

    def RemoveDuplicates(self,head):
        if head is None:
            return None
        else:
            new_head = head
            while head.next is not None:
                if head.data == head.next.data:
                    head.next = head.next.next
                else:
                    head = head.next
            return new_head


ll=Linked_list()
head_new=ll.inserNth(3,0)
head_new=ll.inserNth(5,1)
head_new=ll.inserNth(5,2)
head_new=ll.inserNth(6,3)
head_new=ll.inserNth(6,4)
head_new=ll.inserNth(7,5)
print("Linked list :")
ll.display(head_new)
new_head=ll.RemoveDuplicates(head_new)
print ("new linked list :")
ll.display(new_head)



















