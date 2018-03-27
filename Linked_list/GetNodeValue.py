"""You’re given the pointer to the head node of a linked list and a specific position. Counting backwards from the tail
 node of the linked list, get the value of the node at the given position.
A position of 0 corresponds to the tail, 1 corresponds to the node before the tail and so on."""


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

    def GetNodeValue(self,head,position):
        l = 0
        trail = head
        while (head):
            if l > position:
                trail = trail.next

            l = l + 1
            head = head.next
        return trail.data


ll=Linked_list()
head_new=ll.inserNth(3,0)
head_new=ll.inserNth(4,1)
head_new=ll.inserNth(5,2)
head_new=ll.inserNth(8,3)
head_new=ll.inserNth(3,4)
head_new=ll.inserNth(7,5)
print("Linked list :")
ll.display(head_new)
nodvalue=ll.GetNodeValue(head_new,2)
print("the node value at at 2 from tail is :",nodvalue)











