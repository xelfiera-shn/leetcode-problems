class Solution(object):
    @staticmethod
    def nextPermutation(nums):
        leftIndex = len(nums) - 2
        rightIndex = len(nums) - 1

        checker = False
        while leftIndex >= 0:
            if nums[rightIndex] > nums[leftIndex]:

                nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
                nums[leftIndex + 1 : ] = sorted(nums[leftIndex + 1 : ])

                checker = True
                break

            rightIndex -= 1
            if rightIndex == leftIndex:
                leftIndex -= 1
                rightIndex = len(nums) - 1

        if not checker: nums.sort()