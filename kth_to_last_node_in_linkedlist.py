
# Q: Write a function kth_to_last_node() that takes an integer kk and the head_node of a singly-linked list, and returns the kkth to last node in the list.

"""
  class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# Returns the node with value "Devil's Food" (the 2nd to last node)
kth_to_last_node(2, a)
"""

def kth_to_last_node(k, head):

    # Return the kth to last node in the linked list

    if head is None:
        return None
    first_node = head
    store = []
    while head is not None and head.next is not None:
        store.append(head)
        first_node = first_node.next
    
    
    return store[-k]



