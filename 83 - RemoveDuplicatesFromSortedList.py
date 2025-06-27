class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def deleteDuplicates(head):
        temp = head
        while temp != None and temp.next != None:
            if temp.next.val == temp.val:
                temp.next = temp.next.next

            else:
                temp = temp.next

        return head