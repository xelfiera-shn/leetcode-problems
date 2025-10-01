class Solution(object):
    @staticmethod
    def searchMatrix(matrix, target):
        for row in matrix:
            for number in row:
                if number == target:
                    return True

        return False
    
# Another solution
class Solution(object):
    @staticmethod
    def searchMatrix(matrix, target):
        for i, row in enumerate(matrix):
            if matrix[i][len(row) - 1] == target:
                return True
            
            elif matrix[i][len(row) - 1] < target:
                if i == len(matrix) - 1:
                    return False
                
                continue

            for number in row:
                if number == target:
                    return True
                
        return False
    
# Another solution
class Solution(object):
    @staticmethod
    def searchMatrix(matrix, target):
        expandedMatrix = []
        for row in matrix:
            expandedMatrix += row

        left, right = 0, len(expandedMatrix) - 1
        while left <= right:
            mid = int((left + right) / 2)

            if expandedMatrix[mid] == target:
                return True
            
            elif expandedMatrix[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
    
# Another solution (optimized version of third solution)
class Solution(object):
    @staticmethod
    def searchMatrix(matrix, target):
        rowLength = len(matrix)
        columnLength = len(matrix[0])

        left, right = 0, rowLength * columnLength - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // columnLength
            column = mid % columnLength

            if matrix[row][column] == target:
                return True
            
            elif matrix[row][column] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False