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