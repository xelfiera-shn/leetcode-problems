# You can skip this one.
class Solution(object):
    @staticmethod
    def removeDuplicates(nums):
        index = 0
        for i in range(len(nums) - 1):
            if nums[i] != nums [i + 1]:
                nums[index] = nums[i]
                index += 1
                
        return index