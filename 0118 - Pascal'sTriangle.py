class Solution(object):
    @staticmethod
    def generate(numRows):
        pascalTriangle = [[1]]
        if numRows == 1:
            return pascalTriangle

        def CalculateAndInsertNextRow():
            currentRow = pascalTriangle[-1]
            if len(currentRow) == 1:
                pascalTriangle.append([1, 1])
                return
            
            firstIndex = 0
            secondIndex = 1
            nextRow = []
            while secondIndex < len(currentRow):
                nextRow.append(currentRow[firstIndex] + currentRow[secondIndex])

                firstIndex += 1
                secondIndex += 1

            nextRow.insert(0, 1)
            nextRow.append(1)
            pascalTriangle.append(nextRow)

        for i in range(numRows - 1):
            CalculateAndInsertNextRow()

        return pascalTriangle
    
# Another solution (Combinatorial)
class Solution(object):
    @staticmethod
    def generate(numRows):
        from math import factorial as fc

        triangle = []
        for i in range(numRows):
            row = [0] * (i + 1)
            for j in range(i + 1):
                row[j] = fc(i) / fc(i - j) / fc(j)

            triangle.append(row)

        return triangle