# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        self.tmp = []

        
        def pre(node):
            if not node:
                return
            self.tmp.append(node)
            pre(node.left)
            pre(node.right)

        pre(root)
        #print(self.tmp)

        for i in range(len(self.tmp) -1):
            self.tmp[i].right = self.tmp[i+1]
            self.tmp[i].left = None



        