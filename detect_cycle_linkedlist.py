## Q: Write a function contains_cycle() that takes the first node in a singly-linked 
## list and returns a boolean indicating whether the list contains a cycle.

def contains_cycle(first_node):

    # Check if the linked list contains a cycle
    if first_node:
        node = first_node.next
        cache = set()
        while node:
            cache.add(node)
            
            if node.next == first_node:
                return True
            if node.next.next and node.next.next in cache:
                return True
            if not node.next.next: return False
            # move to the next node
            node = node.next
        
    return False
