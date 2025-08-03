class Solution:
    def myPow(self, x, n):
        if not n: return 1
        if n < 0: return 1 / self.myPow(x, -n)
        if n % 2: return x * self.myPow(x, n - 1)
        else: return self.myPow(x * x, n / 2)

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