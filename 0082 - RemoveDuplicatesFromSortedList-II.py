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
    
# Another solution on the web
class Solution(object):
    @staticmethod
    def deleteDuplicates(head):
        dummyHead = previousNode = ListNode(0)
        dummyHead.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next

                head = head.next
                previousNode.next = head

            else:
                previousNode = previousNode.next
                head = head.next
                
        return dummyHead.next