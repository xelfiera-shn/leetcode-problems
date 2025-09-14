class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def swapPairs(head):
        def processNode(node):
            if node.next == None:
                return node
            
            previousNode = node
            currentNode = node.next
            nextNode = node.next.next

            if nextNode != None:
                nextNode = processNode(nextNode)

            previousNode.next = nextNode
            currentNode.next = previousNode

            return currentNode
        
        return processNode(head) if head else head