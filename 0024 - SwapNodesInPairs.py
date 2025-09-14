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
    
# Another solution
class Solution(object):
    def swapPairs(self, head):
        previousNode, previousNode.next = self, head

        while previousNode.next and previousNode.next.next:
            currentNode = previousNode.next
            nextNode = currentNode.next
            previousNode.next, nextNode.next, currentNode.next = nextNode, currentNode, nextNode.next
            previousNode = currentNode
            
        return self.next