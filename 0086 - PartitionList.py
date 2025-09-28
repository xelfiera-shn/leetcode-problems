class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def partition(head, x):
        lessValueList = []
        moreValueList = []
        while head != None:
            if head.val < x:
                lessValueList.append(head.val)

            else:
                moreValueList.append(head.val)

            head = head.next

        newHead = None
        currentNode = None
        for value in lessValueList + moreValueList:
            if newHead == None:
                newHead = ListNode(value)
                currentNode = newHead
                continue

            newNode = ListNode(value)
            currentNode.next = newNode
            currentNode = currentNode.next

        return newHead