class Solution(object):
    @staticmethod
    def permute(nums):
        permutations = []
        generatePermutations(permutations, [], nums)
        return permutations

def generatePermutations(permutations, candidate, nums):
    if len(nums) == 0:
        permutations.append(candidate)
        return
    
    for i in range(len(nums)):
        newCandidate = candidate[ : ]
        remainNums = nums[ : ]

        newCandidate.append(remainNums[i])
        remainNums.pop(i)

        generatePermutations(permutations, newCandidate, remainNums)

# Another solution using itertools
from itertools import permutations

class Solution(object):
    @staticmethod
    def permute(nums):
        return list(permutations(nums))