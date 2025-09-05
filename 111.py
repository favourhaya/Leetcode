# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        level = 0
        queue = [root]
        while len(queue) > 0:
            n = len(queue)
            level += 1
            
            for _ in range(n):
                curr = queue[0]
                queue = queue[1:]
                if not curr.left and not curr.right:
                    print(curr.val)
                    return level
                if curr.left:
                    queue.append(curr.left)
            
                if curr.right:
                    queue.append(curr.right)

           


        