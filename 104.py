# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        level = 0

        if not root:
            return 0


        while len(queue) > 0:
            size = len(queue)
            level +=1   
            for _ in range(size): 
                curr = queue[0]
                queue = queue[1:]
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
        return level
        


#dfs solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = 1 + self.maxDepth(root.left)
        right = 1+ self.maxDepth(root.right)

        return max(left,right)

            
