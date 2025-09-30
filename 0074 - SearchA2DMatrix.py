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