# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        res = [root.val /1]

        if not root:
            return []

        while len(queue) > 0:
            t = 0
            c = 0
            size = len(queue)
            for _ in range(size):
                curr = queue[0]
                queue = queue[1:]
                if not curr.left and not curr.right:
                    continue
                if curr.left:
                    queue.append(curr.left)
                    t += curr.left.val
                    c += 1
                if curr.right:
                    queue.append(curr.right)
                    t += curr.right.val
                    c+= 1 
            if t != 0 or c != 0:
                res.append(t / c)
            #print(t,c)   
            
        return res       


        