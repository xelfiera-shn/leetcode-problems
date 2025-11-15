# Solution with math.factorial
from math import factorial as fc
class Solution(object):
    @staticmethod
    def getRow(rowIndex):
        row = []
        for index in range(rowIndex + 1):
            row.append(fc(rowIndex) / (fc(rowIndex - index) * fc(index)))

        return row

# Another solution with math.comb
from math import comb
class Solution(object):
    @staticmethod
    def getRow(rowIndex):
        row = []
        for index in range(rowIndex + 1):
            row.append(comb(rowIndex, index))

        return row
    