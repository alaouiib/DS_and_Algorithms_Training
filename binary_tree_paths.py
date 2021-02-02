# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        # stack based solution
        if not root:
            return []

        stack = [(root, str(root.val))]
        res = []
        while stack:
            current, path = stack.pop()
            if not current.left and not current.right:
                res.append(path)

            if current.left:
                stack.append(
                    (current.left, path + '->' + str(current.left.val)))

            if current.right:
                stack.append(
                    (current.right, path + '->' + str(current.right.val)))

        return res
