# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            queue = [root]
            track = [[root.val]]

            while len(queue) > 0:
                tmp = []
                for _ in range(len(queue)):
                    curr = queue[0]
                    queue = queue[1:]
                    if curr.left:
                        tmp.append(curr.left.val)
                        queue.append(curr.left)

                    if curr.right:
                        tmp.append(curr.right.val)
                        queue.append(curr.right)
                    
                if len(tmp) > 0:
                    track.append(tmp)
            return track
        else:
            return []
        

            