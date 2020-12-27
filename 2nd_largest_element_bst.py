
def find_rightmost_soft(root_node):

    current = root_node
    while current:
        if not current.right:
            return current.value
        current = current.right

def find_rightmost(root_node):
    if root_node is None:
        raise ValueError('Tree must have at least 1 node')

    if root_node.right:
        return find_rightmost(root_node.right)
    return root_node.value

# Complexity: O(h) Time and Space, O(1) Space if we use find_rightmost_soft function
# h is the height of the tree
def find_second_largest(root_node):

    # Find the second largest item in the binary search tree
    # idea: find the rightmost node, and take the parentNode if the rightmost node doesn't have a left node
    # else: reiterate the rightmost function on the left node.
    # edge cases: no right subtree existing, and a tree with no root or with 1 node
    # raise error if there is one or no node in the tree
    if (root_node is None or
            (root_node.left is None and root_node.right is None)):
        raise ValueError('Tree must have at least 2 nodes')

    # we dont have a right subtree => 2nd largest is the largest in the left subtree
    if root_node.left and not root_node.right:
        return find_rightmost(root_node.left)

    if root_node.right and (not root_node.right.left and not root_node.right.right):
        return root_node.value

    return find_second_largest(root_node.right)
