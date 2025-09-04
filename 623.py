# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        queue = [root]
        ans = []
        level = 0
        if not root:
            return []

        if level == depth-1:
            tmp = root
            root = TreeNode(val,tmp,None)


        while len(queue) > 0:
            n = len(queue)
            level += 1
            for _ in range(n):
                curr = queue[0]
                queue =  queue[1:]
                if level == depth-1:
                    tmp = curr.left
                    curr.left = TreeNode(val,tmp,None)

                    tmp = curr.right
                    curr.right = TreeNode(val,None,tmp)
                else:
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
        return root

                    
                    



                

