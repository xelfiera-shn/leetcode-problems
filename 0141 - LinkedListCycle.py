class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    @staticmethod
    def hasCycle(head):
        if not head: return False

        memory = set()
        while head:
            if head in memory:
                return True
            
            memory.add(head)
            head = head.next

        return False