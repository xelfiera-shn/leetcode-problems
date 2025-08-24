class Solution(object):
    @staticmethod
    def setZeroes(matrix):
        markedRows = []
        markedColumns = []

        for y in range(len(matrix)):
            for x in range(len(matrix[0])):
                if matrix[y][x] == 0:
                    if y not in markedRows: markedRows.append(y)
                    if x not in markedColumns: markedColumns.append(x)

        for row in markedRows:
            for column in range(len(matrix[0])):
                matrix[row][column] = 0

        for column in markedColumns:
            for row in range(len(matrix)):
                matrix[row][column] = 0