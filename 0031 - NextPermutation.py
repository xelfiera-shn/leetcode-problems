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

# Another solution
class Solution(object):
    @staticmethod
    def nextPermutation(nums):
        pointer = rightIndex = len(nums) - 1

        while pointer > 0 and nums[pointer - 1] >= nums[pointer]:
            pointer -= 1

        leftIndex = pointer
        while leftIndex < rightIndex:
            nums[leftIndex], nums[rightIndex] = nums[rightIndex], nums[leftIndex]
            leftIndex += 1
            rightIndex -= 1

        if pointer > 0:
            pointer -= 1; rightIndex = pointer
            while nums[rightIndex] <= nums[pointer]:
                rightIndex += 1
            nums[pointer], nums[rightIndex] = nums[rightIndex], nums[pointer]