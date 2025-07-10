class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    @staticmethod
    def isSymmetric(root):
        if root.left == None and root.right == None: return True
        if root.left == None or root.right == None: return False

        valueListLeft = []
        valueListRight = []

        EvaluateLeftNode(valueListLeft, root.left)
        EvaluateRightNode(valueListRight, root.right)

        return valueListLeft == valueListRight

def EvaluateLeftNode(valList, node, direction='left'):
    if node.left != None:
        EvaluateLeftNode(valList, node.left)

    valList.append(str(node.val) + 'x') if direction == 'left' else valList.append(str(node.val))

    if node.right != None:
        EvaluateLeftNode(valList, node.right, direction='right')

def EvaluateRightNode(valList, node, direction='right'):
    if node.right != None:
        EvaluateRightNode(valList, node.right)

    valList.append(str(node.val) + 'x') if direction == 'right' else valList.append(str(node.val))

    if node.left != None:
        EvaluateRightNode(valList, node.left, direction='left')

# Another Solution
class Solution(object):
    @staticmethod
    def isSymmetric(root):
        def same(root1, root2):
            if not root1 and not root2: return True
            if not root1 or not root2: return False
            if root1.val != root2.val: return False

            return same(root1.left, root2.right) and same(root1.right, root2.left)
        
        return same(root, root)