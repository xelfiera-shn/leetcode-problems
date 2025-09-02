class Solution(object):
    @staticmethod
    def spiralOrder(matrix):
        matrixHeight = len(matrix)
        matrixWidth = len(matrix[0])
        dpMatrix = [[False] * matrixWidth for _ in range(matrixHeight)]

        orderList = []
        x, y, dx, dy = 0, 0, 1, 0
        for _ in range(matrixHeight * matrixWidth):
            orderList.append(matrix[y][x])
            dpMatrix[y][x] = True

            if dpMatrix[(y + dy) % matrixHeight][(x + dx) % matrixWidth]:
                dy, dx = dx, -dy

            x += dx
            y += dy

        return orderList
    
# Another solution
class Solution(object):
    @staticmethod
    def spiralOrder(self, matrix):
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip( * matrix)[ : : -1])