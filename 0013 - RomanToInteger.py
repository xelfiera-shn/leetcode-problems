class Solution(object):
    @staticmethod
    def romanToInt(s):
        valueDict = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}
        
        value = 0
        for i, char in enumerate(s):
            if i < len(s) - 1 and valueDict[char] < valueDict[s[i + 1]]:
                value -= valueDict[char]

            else:
                value += valueDict[char]

        return value