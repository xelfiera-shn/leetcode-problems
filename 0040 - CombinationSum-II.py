class Solution(object):
    @staticmethod
    def combinationSum2(candidates, target):
        combinations = []
        def backtrack(combination, sum, index):
            for localIndex in range(index, len(candidates)):
                if candidates[localIndex] > target:
                    continue

                localSum = sum + candidates[localIndex]

                if localSum > target: continue

                localCombination = combination[ : : ]
                localCombination.append(candidates[localIndex])
                if localSum == target:
                    if localSum not in combinations:
                        combinations.append(localCombination)

                else:
                    backtrack(localCombination, localSum, localIndex + 1)

        candidates.sort()
        backtrack([], 0, 0)
        print(combinations)
        return combinations
    
Solution.combinationSum2([10,1,2,7,6,1,5], 8)