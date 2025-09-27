class Solution(object):
    @staticmethod
    def sortColors(nums):
        colorDict = {0: [], 1: [], 2: []}

        for num in nums:
            colorDict[num].append(num)

        nums[ : ] = colorDict[0] + colorDict[1] + colorDict[2]

# Another solution
class Solution(object):
    @staticmethod
    def sortColors(nums):
        nums.sort()