# Follow up: Could you solve it without converting the integer to a string?
# Yes, i can. :)
class Solution(object):
    @staticmethod
    def isPalindrome(x):
        if x < 0:
            return False
        
        else:
            i = 0
            reversed = 0
            while pow(10, i) <= x:
                currentDigit = int((x % pow(10, i + 1)) / pow(10, i))
                reversed = (reversed * 10) + currentDigit
                i += 1

            if reversed == x:
                return True
            
            else:
                return False
            
# But, it's so easy with string conversion.
class Solution(object):
    @staticmethod
    def isPalindrome(x):
        return str(x) == str(x)[ : : -1]