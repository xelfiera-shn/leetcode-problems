class Solution(object):
    @staticmethod
    def generateMatrix(n):
        rotations = ['RIGHT', 'DOWN', 'LEFT', 'UP']
        spiralMatrix = [[0 for _ in range(n)] for _ in range(n)]

        xIndex = 0
        yIndex = 0
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