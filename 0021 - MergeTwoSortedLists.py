class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    @staticmethod
    def mergeTwoLists(list1, list2):
        mergedList = ListNode()
        tempNode = mergedList
        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                tempNode.next = list1
                list1 = list1.next
            
            else:
                tempNode.next = list2
                list2 = list2.next
                
            tempNode = tempNode.next

        tempNode.next = list1 if list1 != None else list2

        return mergedList.next