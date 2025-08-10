class Solution(object):
    @staticmethod
    def jump(nums):
        currentIndex = 0
        maxReachableIndex = 0
        minJumpCounts = {0: 0}

        while currentIndex <= maxReachableIndex and currentIndex < len(nums):
            if currentIndex + nums[currentIndex] > maxReachableIndex:
                maxReachableIndex = currentIndex + nums[currentIndex]

                for i in range(currentIndex + 1, currentIndex + nums[currentIndex] + 1):
                    if i not in minJumpCounts: minJumpCounts[i] = minJumpCounts[currentIndex] + 1

            if maxReachableIndex >= len(nums) - 1:
                return minJumpCounts[len(nums) - 1]
            
            currentIndex += 1

        return 0