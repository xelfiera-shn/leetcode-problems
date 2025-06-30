class Solution(object):
    @staticmethod
    def climbStairs(n):
        # This is a fibonacci problem
        x, y = 0, 1
        for i in range(n):
            x, y = y, x + y

        return y