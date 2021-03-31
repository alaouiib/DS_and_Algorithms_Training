
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
# 1st  Solution: O(n) Time and Space
# def kth_to_last_node(k, head):

#     # Return the kth to last node in the linked list

#     if head is None:
#         return None

#     first_node = head
#     store = []
#     while first_node is not None:
#         store.append(first_node)
#         if first_node.next:
#             first_node = first_node.next
#         else: break
    
#     if k == 0 or k > len(store):
#         raise Exception('k is bigger than the length of the store')

#     return store[-k]


# 2nd solution: O(n) time and O(1) space, where n is the length of the list.
def kth_to_last_node(k, head):

    # Return the kth to last node in the linked list

    if head is None:
        return None

    first_node = head
    counter = 1
    
    while first_node.next is not None:
        first_node = first_node.next
        counter += 1
        
    res = head
    
    for i in range(counter-k):
        res = res.next
        
    if k == 0 or k > counter:
        raise Exception('k is bigger than the length of the store')

        
    return res

  """ 
## What We Learned

We listed two good solutions. One seemed to solve the problem in one pass, while the other took two passes. But the single-pass approach didn't take half as many steps, it just took the same steps in a different order.

So don't be fooled: "one pass" isn't always fewer steps than "two passes." Always ask yourself, "Have I actually changed the number of steps?"
  
  """



