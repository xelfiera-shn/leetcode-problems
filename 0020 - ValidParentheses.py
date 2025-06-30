class Solution(object):
    @staticmethod
    def isValid(s):
        bracketDict = {'(': ')', '[': ']', '{': '}'}
            
        brackets = ''
        for i in range(len(s)):
            if brackets == '' and s[i] not in bracketDict:
                return False
                
            else:
                brackets += s[i]
                if s[i] not in bracketDict:
                    if s[i] == bracketDict[brackets[-2]]:
                        brackets = brackets[ : -2]

                    else:
                        return False

        return True if brackets == '' else False