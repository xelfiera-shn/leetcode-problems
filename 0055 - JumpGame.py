# Dynamic programming memoization (Time limit exceeded)
class Solution(object):
    @staticmethod
    def canJump(nums):
        memory = [0 for _ in range(len(nums))]
        memory[-1] = 1 # Set true last index

        def setJumpablity(index):
            if memory[index] != 0: return 1

            for i in range(1, nums[index] + 1):
                if setJumpablity(index + i):
                    memory[index] = 1
                    return 1

        setJumpablity(0)
        return True if memory[0] == 1 else False

# Backtrack - Recursive (Time limit exceeded)
class Solution(object):
    @staticmethod
    def canJump(nums):
        def jump(index):
            if index == len(nums) - 1: return True
            if nums[index] == 0: return False

            for i in range(1, nums[index] + 1):
                if jump(index + i): return True
                
            return False
        
        return jump(0)
    
# Lineer solution on the web, i like it
class Solution(object):
    @staticmethod
    def canJump(nums):
        currentIndex = 0
        maxReachableIndex = 0

        while currentIndex <= maxReachableIndex and currentIndex < len(nums):
            maxReachableIndex = max(maxReachableIndex, currentIndex + nums[currentIndex])

            if maxReachableIndex >= len(nums) - 1:
                return True

            currentIndex += 1

        return False