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

print(Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 60))