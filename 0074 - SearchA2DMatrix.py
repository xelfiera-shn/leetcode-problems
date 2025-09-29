class Solution(object):
    @staticmethod
    def searchMatrix(matrix, target):
        rowLength = len(matrix)
        columnLength = len(matrix[0])
        
        upY, downY = 0, rowLength - 1
        while upY <= downY:
            midY = int((upY + downY) / 2)

            if matrix[midY][columnLength - 1] == target:
                return True
            
            elif matrix[midY][columnLength - 1] < target:
                upY = midY + 1

            else:
                downY = midY - 1

        if rowLength != 1 and upY == rowLength - 1:
            return False
        
        if downY <= 0:
            upY = -1
        
        left, right = 0, columnLength - 1
        while left <= right:
            mid = int((left + right) / 2)

            if matrix[upY + 1][mid] == target:
                return True
            
            elif matrix[upY + 1][mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False
    
Solution.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)