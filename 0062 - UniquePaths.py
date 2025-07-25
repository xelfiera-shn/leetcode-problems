class Solution(object):
    @staticmethod
    def uniquePaths(m, n):
        # Permutations with repetition: (m - 1 + n - 1)! / [(m - 1)!(n - 1)!]
        #                             : Combination(m - 1 + n - 1, m - 1)
        #                             : Combination(m - 1 + n - 1, n - 1)

        numerator = 1
        multiplier = m + n - 2
        for i in range(m - 1):
            numerator *= multiplier
            multiplier -= 1

        denominator = 1
        for i in range(1, m): denominator *= i

        return numerator / denominator
    
# Solution with helper functions
from math import factorial

class Solution(object):
    @staticmethod
    def uniquePaths(m, n):
        return factorial(m + n - 2) / factorial(m - 1) / factorial(n - 1)
    
# Another solution (Memory Limit Exceeded)
from itertools import combinations

class Solution(object):
    @staticmethod
    def uniquePaths(m, n):
        return len(list(combinations(range(m + n - 2), min(m - 1, n - 1))))
    
# Another version of my solution, I saw it on the web
class Solution(object):
    @staticmethod
    def uniquePaths(m, n):
        totalMoves = m + n - 2
        minDistance = min(m - 1, n - 1)
        result = 1
        for i in range(1, minDistance + 1):
            result = result * (totalMoves - i + 1) / i

        return result