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

    def reverse(self,head):
        if not head or not head.next: return head
        newHead = self.reverse(head.next)
        print("head :",head.data)
        head.next.next = head
        head.next = None
        return newHead




ll=Linked_list()
head_new=ll.inserNth(3,0)
head_new=ll.inserNth(4,1)
head_new=ll.inserNth(5,2)
print("linked list after insertion")
ll.display(head_new)
rev_head=ll.reverse(head_new)
ll.display(rev_head)










