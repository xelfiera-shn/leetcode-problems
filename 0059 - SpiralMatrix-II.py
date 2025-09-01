class Solution(object):
    @staticmethod
    def generateMatrix(n):
        rotations = ['RIGHT', 'DOWN', 'LEFT', 'UP']
        spiralMatrix = [[0 for _ in range(n)] for _ in range(n)]

        xIndex, yIndex = 0, 0
        currentRotationIndex = 0
        currentValue = 1
        spiralMatrix[0][0] = 1
        while currentValue < n * n:
            if rotations[currentRotationIndex] == 'RIGHT':
                if xIndex + 1 < n and spiralMatrix[yIndex][xIndex + 1] == 0:
                    currentValue += 1
                    spiralMatrix[yIndex][xIndex + 1] = currentValue
                    xIndex += 1

                else:
                    currentRotationIndex += 1
                    currentRotationIndex %= len(rotations)

            elif rotations[currentRotationIndex] == 'DOWN':
                if yIndex + 1 < n and spiralMatrix[yIndex + 1][xIndex] == 0:
                    currentValue += 1
                    spiralMatrix[yIndex + 1][xIndex] = currentValue
                    yIndex += 1

                else:
                    currentRotationIndex += 1
                    currentRotationIndex %= len(rotations)

            elif rotations[currentRotationIndex] == 'LEFT':
                if xIndex - 1 >= 0 and spiralMatrix[yIndex][xIndex - 1] == 0:
                    currentValue += 1
                    spiralMatrix[yIndex][xIndex - 1] = currentValue
                    xIndex -= 1

                else:
                    currentRotationIndex += 1
                    currentRotationIndex %= len(rotations)

            elif rotations[currentRotationIndex] == 'UP':
                if yIndex - 1 >= 0 and spiralMatrix[yIndex - 1][xIndex] == 0:
                    currentValue += 1
                    spiralMatrix[yIndex - 1][xIndex] = currentValue
                    yIndex -= 1

                else:
                    currentRotationIndex += 1
                    currentRotationIndex %= len(rotations)

        return spiralMatrix
    
# Another solution
class Solution(object):
    @staticmethod
    def generateMatrix(n):
        spiralMatrix = [[0] * n for _ in range(n)]
        
        x, y, dx, dy = 0, 0, 1, 0
        for i in range(n * n):
            spiralMatrix[y][x] = i + 1
            if spiralMatrix[(y + dy) % n][(x + dx) % n]:
                dy, dx = dx, -dy
            
            x += dx
            y += dy

        return spiralMatrix
    
# Another solution too
class Solution(object):
    @staticmethod
    def generateMatrix(self, n):
        spiralMatrix = [[n * n]]
        
        while spiralMatrix[0][0] > 1:
            spiralMatrix = [range(spiralMatrix[0][0] - len(spiralMatrix), spiralMatrix[0][0])] + zip(* spiralMatrix[ : : -1])
        
        return spiralMatrix * (n > 0)