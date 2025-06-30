# You can skip this one.
class Solution(object):
    @staticmethod
    def removeElement(nums, val):
        i = 0
        while i != len(nums):
            if nums[i] == val:
                nums.pop(i)
                continue

            i += 1
            
        return len(nums)