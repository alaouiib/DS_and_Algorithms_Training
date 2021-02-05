# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, 0)]
        res = []
        while len(stack):
            node, depth = stack.pop()

            if not node.left and not node.right:
                # if depth == 0: return True
                if depth not in res:
                    res.append(depth)
                    if (len(res) > 2
                        or (len(res) == 2 and (res[0] - res[1] > 1))
                            or (len(res) == 1 and not stack)):
                        return False

            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))

        return True
