## Q: Write a function contains_cycle() that takes the first node in a singly-linked 
## list and returns a boolean indicating whether the list contains a cycle.

def contains_cycle(first_node):

    # Check if the linked list contains a cycle
    if first_node:
        it = first_node.next
        cache = set()
        while it:
            cache.add(it)
            
            if it.next == first_node:
                return True
            if it.next.next and it.next.next in cache:
                return True
            if not it.next.next: return False
            
            it = it.next
        return False
    else: return False
