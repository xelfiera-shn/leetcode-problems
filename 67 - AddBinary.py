class Solution(object):
    @staticmethod
    def addBinary(a, b):
        sum = ''
        carry = 0
        index = 0
        while index < len(a) or index < len(b):
            digitA = int(a[ : : -1][index]) if index < len(a) else 0
            digitB = int(b[ : : -1][index]) if index < len(b) else 0
            digitSum = digitA + digitB + carry

            sum += str(digitSum % 2)
            carry = int(digitSum / 2)

            index += 1

        return sum[ : : -1] if carry == 0 else (sum + str(carry))[ : : -1]

# Additional method
class Solution(object):
    @staticmethod
    def addBinary(a, b):
        return bin(int(a, 2) + int(b, 2))[2 : ]