class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    @staticmethod
    def minDepth(root):
        if not root: return 0

        minDepth = [None]

        def backtrack(node, depth):
            localDepth = depth + 1
            if node.left or node.right:
                if node.left:
                    backtrack(node.left, localDepth)

                if node.right:
                    backtrack(node.right, localDepth)

            else:
                if not minDepth[0]:
                    minDepth[0] = localDepth
                else:
                    if localDepth < minDepth[0]: minDepth[0] = localDepth

        backtrack(root, 0)
        return minDepth[0]
    
# Another solution
class Solution(object):
    def minDepth(self, root):
        if not root: return 0

        d = map(self.minDepth, (root.left, root.right))
        return 1 + (min(d) or max(d))