class Solution(object):
    @staticmethod
    def searchRange(nums, target):
        positions = [-1, -1]

        leftIndex = 0
        rightIndex = len(nums) - 1
        while leftIndex <= rightIndex:
            if positions[0] < 0:
                if nums[leftIndex] != target: leftIndex += 1
                else: positions[0] = leftIndex

            if positions[1] < 0:
                if nums[rightIndex] != target: rightIndex -= 1
                else: positions[1] = rightIndex

            if positions[0] >= 0 and positions[-1] >= 0: break

        return positions