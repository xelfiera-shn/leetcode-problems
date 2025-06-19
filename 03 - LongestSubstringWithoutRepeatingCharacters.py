class Solution(object):
    @staticmethod
    def lengthOfLongestSubstring(s):
        longestSubstring = []
        substring = []
        for char in s:
            if char in substring:
                longestSubstring = substring if len(substring) > len(longestSubstring) else longestSubstring
                duplicateIndex = substring.index(char)
                substring = substring[duplicateIndex:]
                substring.pop(0)  # Remove the first duplicate char.

            substring.append(char)

        return len(substring) if len(substring) > len(longestSubstring) else len(longestSubstring)