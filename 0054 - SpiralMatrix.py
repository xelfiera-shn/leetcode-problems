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
    
'''
|1 2 3|      |6 9|      |8 7|      |4|  =>  |5|  =>  ||
|4 5 6|  =>  |5 8|  =>  |5 4|  =>  |5|
|7 8 9|      |4 7|

spiral_order([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

= [1, 2, 3] + spiral_order([[6, 9],
                            [5, 8],
                            [4, 7]])

= [1, 2, 3] + [6, 9] + spiral_order([[8, 7],
                                     [5, 4]])

= [1, 2, 3] + [6, 9] + [8, 7] + spiral_order([[4],
                                              [5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + spiral_order([[5]])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + spiral_order([])

= [1, 2, 3] + [6, 9] + [8, 7] + [4] + [5] + []

= [1, 2, 3, 6, 9, 8, 7, 4, 5]
'''