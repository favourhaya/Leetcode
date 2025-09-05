# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 1
        queue = [root]
        ans = [root.val]
        
        while len(queue) > 0:
            n = len(queue)
            level +=  1
            args = []

            if level % 2 == 1:
                i = 0
                tmp = 0
                while i < len(queue) /2:
                    tmp= queue[i].val
                    queue[i].val = queue[-i -1].val
                    queue[-i -1].val = tmp
                    i += 1

            for _ in range(n):
                curr = queue[0]
                queue = queue[1:]
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

                
            
        return root
                


                    