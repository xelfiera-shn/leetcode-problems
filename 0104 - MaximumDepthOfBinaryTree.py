class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    @staticmethod
    def maxDepth(root):
        if root == None: return 0
        maxDepth = [0]
        def moveForward(node, depth):
            newDepth = depth + 1
            if newDepth > maxDepth[0]: maxDepth[0] = newDepth

            if node.left != None:
                moveForward(node.left, newDepth)

            if node.right != None:
                moveForward(node.right, newDepth)

            return
        
        moveForward(root, 0)
        return maxDepth[0]