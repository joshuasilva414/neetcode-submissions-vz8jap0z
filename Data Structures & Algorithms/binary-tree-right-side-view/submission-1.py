# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        vals = []

        def reversePrefix(node, depth):
            if not node:
                return
            if depth >= len(vals):
                vals.append(node.val)
            reversePrefix(node.right, depth+1)
            reversePrefix(node.left, depth+1)
        reversePrefix(root,0)
        return vals