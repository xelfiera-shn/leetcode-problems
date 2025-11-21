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
    
# Another solution
class Solution(object):
    @staticmethod
    def minimumTotal(triangle):
        for y in range(1, len(triangle)):
            for x in range(len(triangle[y])):
                if x > 0 and x < len(triangle[y]) - 1:
                    sum1 = triangle[y - 1][x - 1] + triangle[y][x]
                    sum2 = triangle[y - 1][x] + triangle[y][x]

                    triangle[y][x] = sum1 if sum1 < sum2 else sum2

                elif x == 0:
                    triangle[y][x] = triangle[y - 1][x] + triangle[y][x]

                elif x == len(triangle[y]) - 1:
                    triangle[y][x] = triangle[y - 1][x - 1] + triangle[y][x]

        return min(triangle[-1])