# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
       
        queue = [root]
        fromLeft = False

        if not root:
            return []
        ans = [[root.val]]

        while len(queue) > 0: 
            n = len(queue)
            tmp = []
            for _ in range(n):
                curr = queue[0]
                queue = queue[1:]

                if not curr.left and not curr.right:
                    print("ok")
                    continue
    
                if curr.left:
                    queue.append(curr.left)
                    tmp.append(curr.left.val)
                
                if curr.right:
                    queue.append(curr.right)
                    tmp.append(curr.right.val)
                
            if tmp:
                if fromLeft == True:
                    ans.append(tmp)
                    fromLeft = False
                else:
                    ans.append(tmp[::-1])
                    fromLeft = True
            
        return ans
            

        