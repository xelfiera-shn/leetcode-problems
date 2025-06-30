class Solution(object):
    @staticmethod
    def intToRoman(num):
        valueDict = {1: 'I',
                     5: 'V',
                     10: 'X',
                     50: 'L',
                     100: 'C',
                     500: 'D',
                     1000: 'M',}
        
        power = len(str(num)) - 1
        romanValue = ''
        for i in str(num):
            if int(i) <= 3:
                romanValue += valueDict[pow(10, power)] * int(i)

            elif int(i) == 4:
                romanValue += valueDict[pow(10, power)]
                romanValue += valueDict[5 * pow(10, power)]

            elif int(i) <= 8:
                romanValue += valueDict[5 * pow(10, power)]
                romanValue += valueDict[pow(10, power)] * (int(i) % 5)

            else:
                romanValue += valueDict[pow(10, power)]
                romanValue += valueDict[pow(10, power) * 10]

            power -= 1

        return romanValue