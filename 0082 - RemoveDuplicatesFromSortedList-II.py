class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def deleteDuplicates(head):
        nonDuplicatedList = []
        while head != None:
            nonDuplicatedList.append(head.val)

            check = False
            while head.next != None and head.next.val == nonDuplicatedList[-1]:
                head = head.next
                check = True

            if check:
                nonDuplicatedList.pop()

            head = head.next

        if len(nonDuplicatedList) == 0: return None
        if len(nonDuplicatedList) == 1: return ListNode(nonDuplicatedList[0])

        currentNode = ListNode(nonDuplicatedList[1])
        head = ListNode(nonDuplicatedList[0], currentNode)
        for i in range(2, len(nonDuplicatedList)):
            currentNode.next = ListNode(nonDuplicatedList[i])
            currentNode = currentNode.next

        return head
    
# Another solution (optimized)
class Solution(object):
    @staticmethod
    def deleteDuplicates(head):
        pass