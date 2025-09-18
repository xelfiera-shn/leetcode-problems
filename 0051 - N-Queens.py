class Solution(object):
    @staticmethod
    def solveNQueens(n):
        results = []

        queenPositions = [-1 for x in range(n)]
        def placeQueen(queenPositions, candidate, currentY):
            if currentY >= n:
                results.append(candidate)
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

                    validRow = ''
                    for i in range(n): validRow += '.' if i != currentX else 'Q'

                    validCandidate = candidate[ : ]
                    validCandidate.append(validRow)

                    placeQueen(validQueenPositions, validCandidate, currentY + 1)

        placeQueen(queenPositions, [], 0)

        return results
    
# Another solution
class Solution(object):
    @staticmethod
    def solveNQueens(n):
        state = [['.'] * n for _ in range(n)]
        results = []

        visitedColumns = set()
        visitedDiagonals = set()
        visitedAntidiagonals = set()

        def backtrack(row):
            if row == n:
                results.append([''.join(row) for row in state])
                return
            
            for column in range(n):
                difference = row - column
                sum = row + column
                
                if not (column in visitedColumns or difference in visitedDiagonals or sum in visitedAntidiagonals):
                    visitedColumns.add(column)
                    visitedDiagonals.add(difference)
                    visitedAntidiagonals.add(sum)
                    state[row][column] = 'Q'
                    
                    backtrack(row + 1)

                    visitedColumns.remove(column)
                    visitedDiagonals.remove(difference)
                    visitedAntidiagonals.remove(sum)
                    state[row][column] = '.'

        backtrack(0)
        return results