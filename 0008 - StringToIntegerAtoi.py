class Solution(object):
    @staticmethod
    def myAtoi(s):
        s = s.lstrip()
        sign = 1

        if len(s) > 0:
            if s[0] == '-' or s[0] == '+':
                sign = -1 if s[0] == '-' else 1
                s = s[1 : ]

        else: return 0

        numberString = '0'
        for i in range(len(s)):
            if s[i].isdigit():
                numberString += s[i]

            else: break

        number = int(numberString)
        edgeValue = pow(2, 31) - 1 if sign == 1 else pow(2, 31)

        if number > edgeValue:
            number = edgeValue

        return sign * number