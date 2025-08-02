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
class Solution1(object):
    @staticmethod
    def canJump2(nums):
        def jump(index):
            if index == len(nums) - 1: return True
            if nums[index] == 0: return False

            for i in range(1, nums[index] + 1):
                if jump(index + i): return True
                
            return False
        
        return jump(0)