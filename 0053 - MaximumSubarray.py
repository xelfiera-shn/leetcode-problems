# Memory limit exceeded solution
class Solution(object):
    @staticmethod
    def maxSubArray(nums):
        maxValue = nums[0]

        sumDpMatrix = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        for i in range(len(nums)):
            if i > 0:
                sumDpMatrix[0][i] += sumDpMatrix[0][i - 1] + nums[i]

            else:
                sumDpMatrix[0][i] += nums[i]

            if sumDpMatrix[0][i] > maxValue:
                maxValue = sumDpMatrix[0][i]

        for yIndex in range(len(nums) - 1):
            for xIndex in range(yIndex + 1, len(nums)):
                sumDpMatrix[yIndex + 1][xIndex] = sumDpMatrix[yIndex][xIndex] - nums[yIndex]

                if sumDpMatrix[yIndex + 1][xIndex] > maxValue:
                    maxValue = sumDpMatrix[yIndex + 1][xIndex]

        return maxValue

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
    
# Another solution (Dynamic Programming - Tabulation)
class Solution:
    def maxSubArray(self, nums):
        dpMatrix = [[0] * len(nums) for _ in range(2)]

        dpMatrix[0][0], dpMatrix[1][0] = nums[0], nums[0]
        for i in range(1, len(nums)):
            dpMatrix[1][i] = max(nums[i], nums[i] + dpMatrix[1][i - 1])
            dpMatrix[0][i] = max(dpMatrix[0][i - 1], dpMatrix[1][i])
 
        return dpMatrix[0][-1]
    
# Another solution
class Solution(object):
    def maxSubArray(self, nums):
        maxSoFar = nums[0]
        maxCurrent = nums[0]

        for i in range(1,len(nums)):
            maxCurrent = max(nums[i], maxCurrent + nums[i])
            maxSoFar = max(maxSoFar, maxCurrent)

        return maxSoFar