# This is my solution, but... (Time Limit Exceeded)
class Solution(object):
    @staticmethod
    def longestPalindrome(s):
        longestPolindrome = ''

        candidateLength = len(s)
        while candidateLength >= 0:
            index = 0
            while index + candidateLength <= len(s):
                candidate = s[index : index + candidateLength]
                if candidate == candidate[ : : -1] and len(candidate) > len(longestPolindrome):
                    longestPolindrome = candidate

                index += 1

            candidateLength -= 1

        return longestPolindrome
    
# This is my solution too, but i had some help from comments.
class Solution1(object):
    @staticmethod
    def longestPalindrome(s):
        if len(s) <= 1 or s == s[ : : -1]:
            return s
        
        startIndex, maxLength = 0, 1
        for finishIndex in range(1, len(s)):
            oddCandidate = s[finishIndex - maxLength - 1 : finishIndex + 1]
            evenCandidate = s[finishIndex - maxLength : finishIndex + 1]
            if finishIndex - maxLength - 1 >= 0 and oddCandidate == oddCandidate[ : : -1]:
                startIndex = finishIndex - maxLength - 1
                maxLength += 2

            elif evenCandidate == evenCandidate[ : : -1]:
                startIndex = finishIndex - maxLength
                maxLength += 1

        return s[startIndex : startIndex + maxLength]
    
# Additional solution: Manacher Algorithm, you should definitely take a look.