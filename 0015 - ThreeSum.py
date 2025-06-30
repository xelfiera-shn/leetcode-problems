# Solution, but... (Time Limit Exceeded)
class Solution(object):
    @staticmethod
    def threeSum(nums):
        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0: return [nums]
            
            else: return []

        triplets = []
        xIndex = 0
        while xIndex < len(nums) - 2:
            yIndex = xIndex + 1
            while yIndex < len(nums) - 1:
                zIndex = len(nums) - 1
                while zIndex != yIndex:
                    x = nums[xIndex]
                    y = nums[yIndex]
                    z = nums[zIndex]
                    if x + y + z == 0 and sorted([x, y, z]) not in triplets:
                        triplets.append(sorted([x, y, z]))

                    zIndex -= 1

                yIndex += 1

            xIndex += 1

        return triplets
    
# Modified solution with some help
class Solution(object):
    @staticmethod
    def threeSum(nums):
        triplets = []
        nums.sort()
        for xIndex in range(len(nums) - 2):
            if xIndex > 0 and nums[xIndex] == nums[xIndex - 1]:
                continue

            yIndex, zIndex = xIndex + 1, len(nums) - 1
            while yIndex < zIndex:
                sum = nums[xIndex] + nums[yIndex] + nums[zIndex]
                if sum < 0:
                    yIndex += 1

                elif sum > 0:
                    zIndex -= 1

                else:
                    triplets.append([nums[xIndex], nums[yIndex], nums[zIndex]])
                    while yIndex < zIndex and nums[yIndex] == nums[yIndex + 1]:
                        yIndex += 1

                    while yIndex < zIndex and nums[zIndex] == nums[zIndex - 1]:
                        zIndex -= 1
                        
                    yIndex += 1
                    zIndex -= 1

        return triplets