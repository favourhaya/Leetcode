"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = [root]
        while len(queue) > 0:
            size = len(queue)
            i = 0
            while i  < (size):
              
                curr = queue[0]
                if i < size-1:
                    print("ok")
                    queue[0].next = queue[1]
                 
                
                if curr.left:
                    queue.append(curr.left)
                if  curr.right:
                    queue.append(curr.right)  
                
                #queue[0].next =None
                if len(queue) == 1:
                    queue[0].next = None
                
                queue = queue[1:]
                i +=1
        return root
        