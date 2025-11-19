# Time limit exceeded
class Solution(object):
    @staticmethod
    def minimumTotal(triangle):
        sums = []

        def goForward(row, column, sum):
            if row == len(triangle) - 1:
                sums.append(sum)
                return
            
            for i in range(2):
                goForward(row + 1, column + i, sum + triangle[row + 1][column + i])

        goForward(0, 0, triangle[0][0])
        return min(sums)