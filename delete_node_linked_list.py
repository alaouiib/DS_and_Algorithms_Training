
# Complexity
# O(1) time and O(1) space.

But be careful—there are some potential problems with this implementation:

# First, it doesn't work for deleting the last node in the list. We could change the node we're deleting to have a value of None, but the second-to-last node's next pointer would still point to a node, even though it should be None. This could work—we could treat this last, "deleted" node with value None as a "dead node" or a "sentinel node," and adjust any node traversing code to stop traversing when it hits such a node. The trade-off there is we couldn't have non-dead nodes with values set to None. Instead we chose to throw an exception in this case.
# Second, this technique can cause some unexpected side-effects. For example, let's say we call:


"""
a = LinkedListNode(3)
b = LinkedListNode(8)
c = LinkedListNode(2)

a.next = b
b.next = c

delete_node(b)
"""
# Any references to the input node have now effectively been reassigned to its next node. 
# In our example, we "deleted" the node assigned to the variable b, but in actuality we just gave it a new value (2) and a new next!
# If we had another pointer to b somewhere else in our code and we were assuming it still had its old value (8), that could cause bugs.

# If there are pointers to the input node's original next node, those pointers now point to a "dangling" node (a node that's no longer reachable by walking down our list). 
# In our example above, c is now dangling. If we changed c, we'd never encounter that new value by walking down our list from the head to the tail.

def delete_node(node_to_delete):
# Get the input node's next node, the one we want to skip to
next_node = node_to_delete.next

if next_node:
    # Replace the input node's value and pointer with the next
    # node's value and pointer. The previous node now effectively
    # skips over the input node
    node_to_delete.value = next_node.value
    node_to_delete.next  = next_node.next
else:
    # Eep, we're trying to delete the last node!
    raise Exception("Can't delete the last node with this technique!")
