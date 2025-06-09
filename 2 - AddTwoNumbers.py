class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def addTwoNumbers(l1, l2):
        sum = l1.val + l2.val
        carry = int(sum / 10)
        val = sum % 10

        sumListNode = ListNode(val, None)

        if l1.next is not None and l2.next is not None:
            l1.next.val += carry  # Add to l1.val or l2.val, it doesn't matter.
            sumListNode.next = Solution.addTwoNumbers(l1.next, l2.next)

        elif l1.next is not None and l2.next is None:
            l1.next.val += carry
            sumListNode.next = Solution.addTwoNumbers(l1.next, ListNode())

        elif l1.next is None and l2.next is not None:
            l2.next.val += carry
            sumListNode.next = Solution.addTwoNumbers(ListNode(), l2.next)

        else:
            if carry != 0:
                sumListNode.next = ListNode(carry)
                print(sumListNode.next)

        return sumListNode