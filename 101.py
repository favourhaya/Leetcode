# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def compare(leftroot,rightroot):
            if not leftroot and not rightroot:
                return True
            if not leftroot or not rightroot:
                return False
            if leftroot.val != rightroot.val:
                return False

            ans1 = compare(leftroot.left,rightroot.right) and compare(rightroot.left,leftroot.right)
            return ans1

        return compare(root.left,root.right)