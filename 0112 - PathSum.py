class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    @staticmethod
    def hasPathSum(root, targetSum):
        if not root: return False

        def searchTree(root, currentSum):
            currentSum += root.val
            if currentSum == targetSum and not root.left and not root.right: return True

            if (root.left):
                if (searchTree(root.left, currentSum)): return True

            if (root.right):
                if (searchTree(root.right, currentSum)): return True

            return False
        
        return searchTree(root, 0)