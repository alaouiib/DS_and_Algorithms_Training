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
    current_node = head_of_list
    previous_node = None
    next_node = None

    # Until we have 'fallen off' the end of the list
    while current_node:
        # Copy a pointer to the next element
        # before we overwrite current_node.next
        next_node = current_node.next

        # Reverse the 'next' pointer
        current_node.next = previous_node

        # Step forward in the list
        previous_node = current_node
        current_node = next_node

    return previous_node
