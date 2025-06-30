class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def removeNthFromEnd(head, n):
        nodeDict = {}

        currentNode = head
        index = 1
        while currentNode is not None:
            nodeDict[index] = currentNode
            currentNode = currentNode.next if currentNode.next is not None else None
            index += 1

        target = index - n
        if nodeDict[target] == head:
            return head.next if head.next is not None else None
        
        nodeDict[target - 1].next = nodeDict[target + 1] if n != 1 else None

        return head