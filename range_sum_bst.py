# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.counter = 0

        if not root:
            return 0

        def dfs(root):
            if low <= root.val <= high:
                self.counter += root.val

            if root.left:
                dfs(root.left)

            if root.right:
                dfs(root.right)

        dfs(root)
        return self.counter
