class Solution(object):
    @staticmethod
    def searchInsert(nums, target):
        leftIndex = 0
        rightIndex = len(nums) - 1

        while leftIndex <= rightIndex:
            center = int((leftIndex + rightIndex) / 2)
            if nums[center] == target:
                return center
            
            elif nums[center] > target:
                rightIndex = center - 1

            else:
                leftIndex = center + 1

        return leftIndex