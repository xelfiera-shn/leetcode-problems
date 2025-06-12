class Solution(object):
    @staticmethod
    def strStr(haystack, needle):
        finishIndex = len(needle)
        for i in range(len(haystack) - finishIndex + 1):
            if haystack[i : i + finishIndex] == needle:
                return i
            
        return -1