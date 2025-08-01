class Solution:
    @staticmethod
    def twoSum(nums, target):
        diffDict = {}
        for i, number in enumerate(nums):
            if number in diffDict:
                return [diffDict[number], i]

            else:
                diffDict[target - number] = i

        return None