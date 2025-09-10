# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        self.sum = 0
        def verse(node,s):
            if not node:
                return
            
            if not node.left and not node.right:
                self.sum += int(s + str(node.val))
            
            else:
                verse(node.left,s+str(node.val))
                verse(node.right,s+str(node.val))

        verse(root,"")
        return self.sum
        
        