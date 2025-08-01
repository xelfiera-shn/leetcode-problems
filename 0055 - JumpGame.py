# Time limit exceeded
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