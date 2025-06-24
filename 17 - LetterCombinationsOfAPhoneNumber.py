class Solution(object):
    @staticmethod
    def letterCombinations(digits):
        lettersDict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        indexes = [0 for i in range(len(digits))]

        combinations = []
        while len(digits) > 0:
            combination = ''
            for i in range(len(digits)):
                combination += lettersDict[digits[i]][indexes[i]]

            combinations.append(combination)

            for i in range(len(indexes)):
                index = len(indexes) - 1 - i

                indexes[index] += 1
                if index != 0 and indexes[index] == len(lettersDict[digits[index]]):
                    indexes[index] = 0
                    continue

                else: break

            if indexes[0] == len(lettersDict[digits[0]]): break

        return combinations