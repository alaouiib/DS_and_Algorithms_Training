
# Complexity
# O(1) time and O(1) space.


def delete_node(node_to_delete):

    # Delete the input node from the linked list
    # all cases : beginning, end, middle and one node in list
    node_to_delete.value = node_to_delete.next.value
    node_to_delete.next = node_to_delete.next.next
    
    # ## node at the end, only one node.
    # node_to_delete.value = node_to_delete.next.value
    # node_to_delete.next = None


