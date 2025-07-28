class Solution(object):
    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid):
        rowCount = len(obstacleGrid)
        columnCount = len(obstacleGrid[0])
        cellValidPathCounts = [[0 for x in range(columnCount)] for y in range(rowCount)]

        cellValidPathCounts[0][0] = 1
        for y in range(rowCount):
            for x in range(columnCount):
                if obstacleGrid[y][x] == 1:
                    cellValidPathCounts[y][x] = 0
                    continue

                if x > 0: cellValidPathCounts[y][x] += cellValidPathCounts[y][x - 1]

                if y > 0: cellValidPathCounts[y][x] += cellValidPathCounts[y - 1][x]

        return cellValidPathCounts[-1][-1]
    
# Backtracking solution but time limit exceeded
class Solution(object):
    @staticmethod
    def uniquePathsWithObstacles(obstacleGrid):
        rowCount = len(obstacleGrid)
        columnCount = len(obstacleGrid[0])

        validPathCount = [0]
        def move(currentX, currentY):
            if obstacleGrid[currentY][currentX] == 1: return
            
            if currentY == rowCount - 1 and currentX == columnCount - 1:
                validPathCount[0] += 1
                return

            if currentX + 1 < columnCount: move(currentX + 1, currentY)

            if currentY + 1 < rowCount: move(currentX, currentY + 1)

        move(0, 0)

        return validPathCount[0]