class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class Doubly:
    def __init__(self,head=None):
        self.head=head

    def display(self, head):
        if head:
            print(head.data)
            self.display(head.next)


    def SortedInsert(self,head, data):
        if head is None:
            return Node(data)
        else:
            new_node = Node(data)
            if head.data >= new_node.data:
                new_node.next = head
                head.prev = new_node
                head = new_node
            else:
                back_node = head
                fwd_node = head
                while (fwd_node is not None and fwd_node.data < new_node.data):
                    back_node = fwd_node
                    fwd_node = fwd_node.next
                if fwd_node is None:
                    back_node.next = new_node
                    new_node.prev = back_node
                else:
                    new_node.next = fwd_node
                    fwd_node.prev = new_node
                    back_node.next = new_node

        return head

    def Reverse(self,head):
        curr = None
        while head:
            nxt = head.next
            curr = head
            head.next = head.prev
            head.prev = nxt
            head = nxt

        return curr




Dobj=Doubly()
head_new=Dobj.SortedInsert(None,1)
head_new=Dobj.SortedInsert(head_new,2)
head_new=Dobj.SortedInsert(head_new,4)
head_new=Dobj.SortedInsert(head_new,5)
Dobj.display(head_new)
print("\n")
rev_head=Dobj.Reverse(head_new)
Dobj.display(rev_head)