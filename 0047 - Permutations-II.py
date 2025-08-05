class Solution(object):
    @staticmethod
    def permuteUnique(nums):
        permutations = []

        def generatePermutations(numbers, candidate):
            if len(candidate) == len(nums):
                permutations.append(candidate)
                return
            
            lastCheckpoint = None
            for i in range(len(numbers)):
                if numbers[i] == lastCheckpoint:
                    continue

                else:
                    newCandidate = candidate[ : ]
                    remainNumbers = numbers[ : ]

                    newCandidate.append(remainNumbers[i])
                    remainNumbers.pop(i)

                    generatePermutations(remainNumbers, newCandidate)

                    lastCheckpoint = numbers[i]
            
        nums.sort()
        generatePermutations(nums, [])

        return permutations
    
print(Solution.permuteUnique([0, 4, 1, 1]))

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