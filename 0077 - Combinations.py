class Solution(object):
    @staticmethod
    def combine(n, k):
        combinations = []
        GenerateCombinations(combinations, [], 0, n, k)

        return combinations

def GenerateCombinations(combinations, candidate, index, n, k):
    if len(candidate) == k:
        combinations.append(candidate)
        return
    
    for i in range(index, n):
        newCandidate = candidate.copy()
        newCandidate.append(i + 1)
        GenerateCombinations(combinations, newCandidate, i + 1, n, k)

# Another backtrack solution
class Solution:
    @staticmethod
    def combine(n, k):
        results = []
        candidate = []

        def backtrack(start):
            if len(candidate) == k:
                results.append(candidate[ : ])
                return
            
            for num in range(start, n + 1):
                candidate.append(num)
                backtrack(num + 1)
                candidate.pop()

        backtrack(1)
        return results

# Another solution
from itertools import combinations

class Solution:
    @staticmethod
    def combine(n, k):
        return (list(combinations(range(1,n+1), k)))