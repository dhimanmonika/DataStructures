class Node(object):
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next=next_node

class Linked_list:
    def __init__(self):
        self.head=None

    def insertAtBeg(self,data):
        cur=Node(data,self.head)
        self.head=cur
        return self.head

    def display(self,head):
        if head:
            print(head.data)
            self.display(head.next)

    def del_Node(self,position):
        if position == 0:
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next

        else:
            nxt = self.head
            for i in range(position):
                prev = nxt
                nxt = nxt.next
            prev.next = nxt.next

        return self.head

ll=Linked_list()
head_new=ll.insertAtBeg(1)
head_new=ll.insertAtBeg(2)
head_new=ll.insertAtBeg(3)
head_new=ll.insertAtBeg(4)
print("before del :")
ll.display(head_new)
head_new=ll.del_Node(1)
print("after del :")
ll.display(head_new)




