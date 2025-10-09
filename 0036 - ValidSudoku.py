class Solution(object):
    @staticmethod
    def isValidSudoku(board):
        checkRowAndColumnTable = [[[], []] for _ in range(9)]
        check3x3GridTable = [[[] for _ in range(3)] for _ in range(3)]

        for yIndex in range(len(board)):
            for xIndex in range(len(board[yIndex])):
                char = board[yIndex][xIndex]

                if char == '.': continue

                # Check column
                if xIndex in checkRowAndColumnTable[int(char) - 1][0]: return False
                
                checkRowAndColumnTable[int(char) - 1][0].append(xIndex)

                # Check row
                if yIndex in checkRowAndColumnTable[int(char) - 1][1]: return False
                
                checkRowAndColumnTable[int(char) - 1][1].append(yIndex)

                # Check 3x3 grid
                divisionX = xIndex // 3
                divisionY = yIndex // 3
                if char in check3x3GridTable[divisionY][divisionX]: return False
                
                check3x3GridTable[divisionY][divisionX].append(char)

        return True

# Another solution
class Solution(object):
    @staticmethod
    def isValidSudoku(board):
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        grids = [set() for _ in range(9)]

        for yIndex in range(9):
            for xIndex in range(9):
                char = board[yIndex][xIndex]

                if char == '.': continue

                # Check row
                if char in rows[yIndex]: return False
                
                rows[yIndex].add(char)

                # Check column
                if char in columns[xIndex]: return False
                
                columns[xIndex].add(char)

                # Check 3x3 grid
                gridIndex = (xIndex // 3) * 3 + (yIndex // 3)
                if char in grids[gridIndex]: return False
                
                grids[gridIndex].add(char)

        return True