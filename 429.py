"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        queue = [root]
        tmp = []
        output = []

        if not root:
            return []
        while len(queue) > 0:
            
            tmp = []
            size = len(queue)

            for _ in range(size):
                curr = queue[0]
                queue = queue[1:]
                tmp.append(curr.val)
                if curr.children:
                    queue.extend(curr.children)

            output.append(tmp)

        return output
            
                
        