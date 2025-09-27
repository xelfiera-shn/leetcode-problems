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

# Another solution (Dutch National Flag)
class Solution(object):
    @staticmethod
    def sortColors(nums):
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1
                
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1