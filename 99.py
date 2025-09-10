# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.tmp = []

        def check(root):
            if not root:
                return
            
            check(root.left)
            self.tmp.append(root)
            check(root.right)
        
        check(root)

        rev = sorted(n.val for n in self.tmp)
        for i in range(len(self.tmp)):
            self.tmp[i].val =rev[i]