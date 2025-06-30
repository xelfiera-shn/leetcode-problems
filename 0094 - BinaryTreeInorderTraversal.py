class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    @staticmethod
    def inorderTraversal(root):
        inorderedValues = []
        if root != None:
            EvaluateNode(inorderedValues, root)

        return inorderedValues
    
def EvaluateNode(valList, node):
    if node.left != None:
        EvaluateNode(valList, node.left)

    valList.append(node.val)

    if node.right != None:
        EvaluateNode(valList, node.right)

# Another solution, i like it.
class Solution(object):
    def inorderTraversal(self, root):
        if root is None:
            return []
        
        return (self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right))