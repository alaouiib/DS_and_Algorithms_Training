## Q: Write a function contains_cycle() that takes the first node in a singly-linked 
## list and returns a boolean indicating whether the list contains a cycle.

# Complexity: Time O(n), Space O(n):
def contains_cycle(first_node):

    # Check if the linked list contains a cycle
    if first_node:
        node = first_node
        cache = set()
        while node:
            # If the current node is already in our set, we have a cycle. Return True.
            if node.next and node.next in cache:
                return True
                
            # If the current node is None we've hit the end of the list. Return False.
            if not node.next: return False
            
            # Else throw the current node in our set and keep going.
            cache.add(node)

            node = node.next
        
    
    return False
