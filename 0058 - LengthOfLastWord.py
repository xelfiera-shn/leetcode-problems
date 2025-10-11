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
        s = list(s)
        lastWord = []

        isWord = False
        for i in range(len(s)):
            if not isWord and s[len(s) - 1 - i] == ' ':
                continue

            isWord = True
            if s[len(s) - 1 - i] != ' ':
                lastWord.append(s[len(s) - 1 - i])
                continue

            break

        return len(lastWord)