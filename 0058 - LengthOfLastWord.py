class Solution(object):
    @staticmethod
    def lengthOfLastWord(s):
        s = s.strip()
        words = s.split(' ')
        return len(words[-1])

# Another format
class Solution(object):
    @staticmethod
    def lengthOfLastWord(s):
        return len(s.strip().split(' ')[-1])
    
# Another solution
class Solution(object):
    @staticmethod
    def lengthOfLastWord(s):
        pass