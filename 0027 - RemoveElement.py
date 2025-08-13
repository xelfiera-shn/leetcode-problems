# You can skip this one.
class Solution(object):
    @staticmethod
    def removeElement(nums, val):
        index = 0
        while index != len(nums):
            if nums[index] == val:
                nums.pop(index)
                continue

            index += 1
            
        return len(nums)