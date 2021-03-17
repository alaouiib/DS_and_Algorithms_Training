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




"""
Explanation:
let's make two variables, slow_runner and fast_runner. 
We’ll start both on the first node, and every time slow_runner advances one node,
we’ll have fast_runner advance two nodes.

If fast_runner catches up with slow_runner, we know we have a loop.
If not, eventually fast_runner will hit the end of the linked list and we'll know we don't have a loop.
"""
# Complexity: Time O(n), Space O(1):
def contains_cycle_space_optimised(first_node):

    # Check if the linked list contains a cycle
    if first_node:
        # cache = set()
        slow_runner = first_node
        fast_runner = first_node
        counter = 0
        while slow_runner:
            while fast_runner:
                counter = counter + 1
                fast_runner = fast_runner.next
                if counter == 2:
                    slow_runner = slow_runner.next
                    counter = 0
                if fast_runner is slow_runner: return True
                if fast_runner is None: return False
return False


"""
optimised code from interview cake:

  def contains_cycle(first_node):
    # Start both runners at the beginning
    slow_runner = first_node
    fast_runner = first_node

    # Until we hit the end of the list
    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        # Case: fast_runner is about to "lap" slow_runner
        if fast_runner is slow_runner:
            return True

    # Case: fast_runner hit the end of the list
    return False
"""
