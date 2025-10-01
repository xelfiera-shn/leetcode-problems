class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def deleteDuplicates(head):
        if head == None or head.next == None:
            return head
        
        nonDuplicatedList = []

        while head.next != None:
            nonDuplicatedList.append(head.val)

            while head.next != None and head.next.val == nonDuplicatedList[-1]:
                head = head.next

            head = head.next

        currentNode = ListNode(nonDuplicatedList[1])
        head = ListNode(nonDuplicatedList[0], currentNode)
        for i in range(2, len(nonDuplicatedList)):
            currentNode.next = ListNode(nonDuplicatedList[0])
            currentNode = currentNode.next

        return head