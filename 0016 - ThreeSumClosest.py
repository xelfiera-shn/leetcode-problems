class Solution(object):
    @staticmethod
    def threeSumClosest(nums, target):
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]

        for xIndex in range(len(nums) - 2):
            yIndex = xIndex + 1
            zIndex = len(nums) - 1
            while yIndex < zIndex:
                sum = nums[xIndex] + nums[yIndex] + nums[zIndex]
                if sum == target: return sum

                if abs(closestSum - target) > abs(sum - target): closestSum = sum

                if target > sum: yIndex += 1

                elif target < sum: zIndex -= 1

        return closestSum