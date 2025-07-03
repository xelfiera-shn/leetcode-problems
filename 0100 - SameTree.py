class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    @staticmethod
    def isSameTree(p, q):
        if not p and not q:
            return True
        
        elif not p or not q:
            return False
        
        return CompareNodes(p, q)

def CompareNodes(node1, node2):
    if node1.val != node2.val:
        return False
    
    else:
        if node1.left and node2.left:
            if not CompareNodes(node1.left, node2.left):
                return False
            
        elif node1.left or node2.left:
            return False
        
        if node1.right and node2.right:
            if not CompareNodes(node1.right, node2.right):
                return False
            
        elif node1.right or node2.right:
            return False
        
        return True
    
# Another Solution I have implemented.
class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        
        elif not p or not q:
            return False
        
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)