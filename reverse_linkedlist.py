"""
Q: reverse a linked list

  class LinkedListNode(object):

    def __init__(self, value):
        self.value = value
        self.next  = None
"""


# In-place reversal
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

  # Out-of-place reversal
  
  # out place using stack
"""
Using Stack:

-Store the nodes(values and address) in the stack until all the values are entered.
-Once all entries are done, Update the Head pointer to the last location(i.e the last value).
-Start popping the nodes(value and address) and store them in the same order until the stack is empty.
-Update the next pointer of last Node in the stack by NULL.

"""
def reverse_using_stack(head_of_list):
    if not head_of_list:
        return None
        
    stack = []
    while head_of_list:
        stack.append(head_of_list)
        head_of_list = head_of_list.next
        
    head = stack.pop()
    temp = head
       
    # head = None
    while stack:
        node = stack.pop()
        
        temp.next = node
        temp = node
    temp.next = None
    
    return head
    
