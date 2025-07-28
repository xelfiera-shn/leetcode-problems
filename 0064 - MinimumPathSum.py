class Solution(object):
    @staticmethod
    def minPathSum(grid):
        rowCount = len(grid)
        columnCount = len(grid[0])
        cellMinimumPathValues = [[0 for x in range(columnCount)] for y in range(rowCount)]

        cellMinimumPathValues[0][0] = grid[0][0]
        for y in range(rowCount):
            for x in range(columnCount):
                cellMinimumPathValues[y][x] = grid[y][x]

                if x > 0 and y > 0:
                    if cellMinimumPathValues[y][x - 1] < cellMinimumPathValues[y - 1][x]:
                        cellMinimumPathValues[y][x] += cellMinimumPathValues[y][x - 1]

                    else:
                        cellMinimumPathValues[y][x] += cellMinimumPathValues[y - 1][x]

                elif x > 0:
                    cellMinimumPathValues[y][x] += cellMinimumPathValues[y][x - 1]

                elif y > 0:
                    cellMinimumPathValues[y][x] += cellMinimumPathValues[y - 1][x]

        return cellMinimumPathValues[-1][-1]

# Backtracking solution but time limit exceeded
class Solution(object):
    @staticmethod
    def minPathSum(grid):
        rowCount = len(grid)
        columnCount = len(grid[0])

        minimumPathValue = [-1]
        def move(currentValue, currentX, currentY):
            currentValue += grid[currentY][currentX]

            if currentY == rowCount - 1 and currentX == columnCount - 1:
                if currentValue < minimumPathValue[0] or minimumPathValue[0] == -1:
                    minimumPathValue[0] = currentValue

                return

            if currentX + 1 < columnCount: move(currentValue, currentX + 1, currentY)

            if currentY + 1 < rowCount: move(currentValue, currentX, currentY + 1)

        move(0, 0, 0)

        return minimumPathValue[0]