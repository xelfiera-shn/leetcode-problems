class Solution(object):
    @staticmethod
    def maxArea(height):
        maxArea = 0
        leftIndex = 0
        rightIndex = len(height) - 1
        while leftIndex != rightIndex:
            maxArea = max(maxArea, min(height[leftIndex], height[rightIndex]) * (rightIndex - leftIndex))

            if height[leftIndex] >= height[rightIndex]: rightIndex -= 1
            else: leftIndex += 1
        
        return maxArea