class Solution(object):
    @staticmethod
    def nextPermutation(nums):
        leftIndex = len(nums) - 2
        rightIndex = len(nums) - 1

        checker = False
        while leftIndex >= 0:
            if nums[rightIndex] > nums[leftIndex]:

                # 2, 3, 1 --> 3, 2, 1 --> 3, 1, 2
                nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
                nums[rightIndex : ] = sorted(nums[rightIndex : ])

                print(nums)
                checker = True
                break

            rightIndex -= 1
            if rightIndex == leftIndex:
                leftIndex -= 1
                rightIndex = len(nums) - 1

        if not checker: nums.sort()

print(Solution.nextPermutation([2, 3, 1]))