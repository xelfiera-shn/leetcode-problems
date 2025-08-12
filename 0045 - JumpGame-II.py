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

# Another solution
class Solution(object):
    @staticmethod
    def jump(nums):
        jumpCount = 0
        currentReachableIndex = 0
        maxReachableIndex = 0

        for i in range(len(nums) - 1):
            maxReachableIndex = max(maxReachableIndex, i + nums[i])
            if i == currentReachableIndex:
                jumpCount += 1
                currentReachableIndex = maxReachableIndex

        return jumpCount