class Solution:
    @staticmethod
    def myPow(x, n):
        if not n: return 1
        if n < 0: return 1 / Solution.myPow(x, -n)
        if n % 2: return x * Solution.myPow(x, n - 1)
        else: return Solution.myPow(x * x, n / 2)

# Another solution with Python
class Solution(object):
    @staticmethod
    def myPow(x, n):
        return pow(x, n)

# Another solution with Python
class Solution(object):
    @staticmethod
    def myPow(x, n):
        return x**n