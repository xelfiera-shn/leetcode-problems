class Solution(object):
    @staticmethod
    def longestCommonPrefix(strs):
        strs = sorted(strs) # Sort alphabetically
        
        first = strs[0]
        last = strs[-1]
        commonPrefix = ''
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                commonPrefix += first[i]
                
            else:
                break

        return commonPrefix