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

    def has_cycle(self,head):
        if head is None:
            return 0
        else:
            l = []
            while head:
                if head.data in l:
                    return 1
                else:
                    l.append(head.data)
                head = head.next
            return 0


ll=Linked_list()
head_new=ll.inserNth(3,0)
head_new=ll.inserNth(4,1)
head_new=ll.inserNth(5,2)
head_new=ll.inserNth(8,3)
head_new=ll.inserNth(3,4)
print("Linked list :")
ll.display(head_new)
hascycle=ll.has_cycle(head_new)
if(hascycle):
    print("Linked list has cycle")
else :
    print("No cycle in Linked list")







