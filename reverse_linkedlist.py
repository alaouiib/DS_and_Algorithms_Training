"""
Q: reverse a linked list

  class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None
"""


## O(n) time and O(1) space.
## We pass over the list only once, and maintain a constant number
## of variables in memory.

def reverse(head_of_list):

    # Reverse the linked list in place
    current_node = head_of_list
    previous_node = None
    next_node = None
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
        

    return previous_node
