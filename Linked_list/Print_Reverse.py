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

    def print_rev(self,head):
        if head:
            self.print_rev(head.next)
            print(head.data)




ll=Linked_list()
head_new=ll.inserNth(3,0)
head_new=ll.inserNth(4,1)
head_new=ll.inserNth(5,2)
ll.print_rev(head_new)


