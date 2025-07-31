class Solution(object):
    @staticmethod
    def totalNQueens(n):
        resultCount = [0]

        queenPositions = [-1 for x in range(n)]
        def placeQueen(queenPositions, currentY):
            if currentY >= n:
                resultCount[0] += 1
                return
            
            for currentX in range(n):
                check = True

                checkerY = 0
                while check and checkerY < n:
                    if queenPositions[checkerY] == currentX: check = False
                    checkerY += 1

                checkerX, checkerY = currentX - 1, currentY - 1
                while check and checkerX >= 0 and checkerY >= 0:
                    if queenPositions[checkerY] == checkerX: check = False
                    checkerX -= 1
                    checkerY -= 1

                checkerX, checkerY = currentX + 1, currentY - 1
                while check and checkerX < n and checkerY >= 0:
                    if queenPositions[checkerY] == checkerX: check = False
                    checkerX += 1
                    checkerY -= 1

                if check:
                    validQueenPositions = queenPositions[ : ]
                    validQueenPositions[currentY] = currentX

                    placeQueen(validQueenPositions, currentY + 1)

        placeQueen(queenPositions, 0)

        return resultCount[0]