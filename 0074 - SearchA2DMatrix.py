class Solution(object):
    @staticmethod
    def searchMatrix(matrix, target):
        for row in matrix:
            for number in row:
                if number == target:
                    return True

        return False