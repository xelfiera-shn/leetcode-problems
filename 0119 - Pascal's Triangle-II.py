from math import factorial as fc
class Solution(object):
    @staticmethod
    def getRow(rowIndex):
        if rowIndex == 0: return [1]
        
        row = [1]
        for index in range(1, rowIndex):
            row.append(fc(rowIndex) / (fc(rowIndex - index) * fc(index)))

        row.append(1)
        return row