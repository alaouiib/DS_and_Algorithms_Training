import unittest

# Complexity: O(n) Time and Space
def is_balanced(tree_root):
    # Determine if the tree is superbalanced
    # DFS, and keep track of the depth
    # some questions i ve asked !
    
    # how to traverse the tree ? 
    
    ## => in our case, we are using DFS, so we ll keep appending 
    ## nodes to the nodes' stack if they aren't leaves
    
    # how to know if there is still elements in the tree?
    ## in other words, how to traverse all the elements ?
    ## => by using a while loop on the size of our stack
    
    # how to get to the leaves quickly ? and how to know if it's a leaf
    # => by using DFS traversal, => there is no right and left
    
    

    if tree_root is None:
        return False
    # we should not have more than 2 elements
    # O(1) space, because it ll never hold more than 2 elements
    depths = []
    # stack to store tuples of (node, depth) 
    # O(d) space, d is the depth of the tree,
    # bcz we are doing dfs, it will store at most the number 
    # of levels in the tree from the root node down to the lowest node
    nodes = []
    nodes.append((tree_root,0))
    
    # while there is still nodes in the stack (=> we didn't hit a leaf)
    while len(nodes):
        node, depth = nodes.pop()
        
        # 2 cases, if it is a leaf or not
        ## case 1: leaf
        if not node.left and not node.right:
            if depth not in depths:
                depths.append(depth)
                
                # Two ways we might now have an unbalanced tree:
                #   1) more than 2 different leaf depths
                #   2) 2 leaf depths that are more than 1 apart
                
                if len(depths) > 2 or (len(depths) == 2 and abs(depths[0] - depths[1]) >1):
                    return False
            
        ## case 2: node
        else:
            # check first if we have a right or left node, then append
            if node.left:
                nodes.append((node.left,depth + 1))
            if node.right:
                nodes.append((node.right, depth + 1))
        
    return True


















# Tests

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_full_tree(self):
        tree = Test.BinaryTreeNode(5)
        left = tree.insert_left(8)
        right = tree.insert_right(6)
        left.insert_left(1)
        left.insert_right(2)
        right.insert_left(3)
        right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_leaves_at_the_same_depth(self):
        tree = Test.BinaryTreeNode(3)
        left = tree.insert_left(4)
        right = tree.insert_right(2)
        left.insert_left(1)
        right.insert_right(9)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_one(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right.insert_right(7)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_two(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right_right = right.insert_right(7)
        right_right.insert_right(8)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_total(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right.insert_left(8)
        right.insert_right(5)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_subtrees_superbalanced(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_both_subtrees_superbalanced_two(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(2)
        right = tree.insert_right(4)
        left.insert_left(3)
        left_right = left.insert_right(7)
        left_right.insert_right(8)
        right_right = right.insert_right(5)
        right_right_right = right_right.insert_right(6)
        right_right_right.insert_right(9)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_at_different_levels(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(2)
        left_left = left.insert_left(3)
        left.insert_right(4)
        left_left.insert_left(5)
        left_left.insert_right(6)
        right = tree.insert_right(7)
        right_right = right.insert_right(8)
        right_right_right = right_right.insert_right(9)
        right_right_right.insert_right(10)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_only_one_node(self):
        tree = Test.BinaryTreeNode(1)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_linked_list_tree(self):
        tree = Test.BinaryTreeNode(1)
        right = tree.insert_right(2)
        right_right = right.insert_right(3)
        right_right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)
