# The solution where performance doesn't matter
class Solution(object):
    @staticmethod
    def permuteUnique(nums):
        permutations = []

        def generatePermutations(numbers, candidate):
            if len(numbers) == 0:
                if candidate not in permutations:
                    permutations.append(candidate)

                return

            for i in range(len(numbers)):
                newCandidate = candidate[ : ]
                remainNumbers = numbers[ : ]

                newCandidate.append(remainNumbers[i])
                remainNumbers.pop(i)

                generatePermutations(remainNumbers, newCandidate[ : ])

        generatePermutations(nums, [])

        return permutations