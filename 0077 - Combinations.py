class Solution(object):
    @staticmethod
    def combine(n, k):
        combinations = []
        GenerateCombinations(combinations, [], 0, n, k)

        return combinations

def GenerateCombinations(combinations, candidate, index, n, k):
    if len(candidate) == k:
        combinations.append(candidate)
        print(candidate)

    for i in range(index, n):
        candidate += [i + 1]
        GenerateCombinations(combinations, candidate, i + 1, n, k)

Solution.combine(4, 2)