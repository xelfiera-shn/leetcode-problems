# My solution
class Solution(object):
    # Rotation in the coordinate plane by 90-degrees
    @staticmethod
    def rotate(matrix):
        xIndex = 0
        yIndex = 0
        lineRange = len(matrix) - 1
        while yIndex < int(len(matrix) / 2):
            currentX = xIndex
            currentY = yIndex
            tempValue = matrix[currentY][currentX]
            for iteration in range(4):
                # Calculate new position after 90-degree clockwise rotation
                # Formula: (x,y) -> (y, n-1-x) where n is matrix size
                newX = -currentY + len(matrix) - 1
                newY = currentX
                matrix[newY][newX], tempValue = tempValue, matrix[newY][newX]
                currentX = newX
                currentY = newY

            xIndex += 1
            if xIndex >= lineRange:
                yIndex += 1
                xIndex = yIndex
                lineRange -= 1

# Common solution on the web
class Solution(object):
    @staticmethod
    def rotate(matrix):
        # Transpose matrix
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse matrix
        for i in range(n):
            for j in range(n//2):
                matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]