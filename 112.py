# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.ans = []

        if not root:
            return False
        
       

        def traverse(node,s):
            if not node:
                return False
            
            if not node.left and not node.right:
                return node.val == s

        
            
            left = traverse(node.left,s-node.val)
            right = traverse(node.right,s-node.val)

            return left or right
        return traverse(root,targetSum)


        