class Solution(object):
    @staticmethod
    def maxSubArray(nums):
        pass

# Time limit exceeded solution
class Solution(object):
    @staticmethod
    def maxSubArray(nums):
        maxValue = nums[0]

        for xIndex in range(len(nums)):
            localSum = 0

            yIndex = xIndex
            while yIndex < len(nums):
                localSum += nums[yIndex]

                if localSum > maxValue:
                    maxValue = localSum

                yIndex += 1

        return maxValue