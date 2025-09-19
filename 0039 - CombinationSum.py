class Solution(object):
    @staticmethod
    def combinationSum(candidates, target):
        results = []
        candidates.sort()

        def calculateCombination(combination, sum):
            for candidate in candidates:
                newSum = sum + candidate
                newCombination = combination[ : : ]
                newCombination.append(candidate)
                newCombination.sort()

                if newSum == target:
                    if not newCombination in results:
                        results.append(newCombination)

                    break

                elif newSum < target:
                    calculateCombination(newCombination[ : : ], newSum)

        calculateCombination([], 0)
        return results