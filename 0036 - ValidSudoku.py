class Solution(object):
    @staticmethod
    def isValidSudoku(board):
        checkRowAndColumnTable = {
            '0': [[], []],
            '1': [[], []],
            '2': [[], []],
            '3': [[], []],
            '4': [[], []],
            '5': [[], []],
            '6': [[], []],
            '7': [[], []],
            '8': [[], []],
            '9': [[], []]
        }

        check3x3GridTable = {
            (0, 0): [],
            (0, 1): [],
            (0, 2): [],
            (1, 0): [],
            (1, 1): [],
            (1, 2): [],
            (2, 0): [],
            (2, 1): [],
            (2, 2): []
        }

        for yIndex in range(len(board)):
            for xIndex in range(len(board[yIndex])):
                char = board[yIndex][xIndex]
                if char == '.': continue

                # Check column
                if xIndex in checkRowAndColumnTable[char][0]: return False

                else: checkRowAndColumnTable[char][0].append(xIndex)

                # Check row
                if yIndex in checkRowAndColumnTable[char][1]: return False

                else: checkRowAndColumnTable[char][1].append(yIndex)

                # Check 3x3 grid
                divisionX = xIndex // 3
                divisionY = yIndex // 3
                if char in check3x3GridTable[(divisionY, divisionX)]: return False

                else: check3x3GridTable[(divisionY, divisionX)].append(char)

        return True