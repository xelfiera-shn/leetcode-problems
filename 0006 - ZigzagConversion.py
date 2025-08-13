class Solution(object):
    @staticmethod
    def convert(s, numRows):
        if numRows == 1: return s

        patternLenght = 2 * numRows - 2
        numColumns = int(len(s) / patternLenght) * (numRows - 1)
        numColumns += 1 if len(s) % patternLenght <= numRows else ((len(s) % patternLenght) % numRows) + 1
        matrix = [[None for x in range(numColumns)] for y in range(numRows)]

        matrix[0][0] = s[0]

        x, y = 0, 0
        for i in range(len(s)):
            matrix[y][x] = s[i]

            if numRows > (i + 1) % patternLenght != 0:
                y += 1

            else:
                x += 1
                y -= 1

        return ''.join(char for row in matrix for char in row if char is not None)

# This isn't my solution, but i like it.
class Solution(object):
    @staticmethod
    def convert(s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rowIndex, dx = 0, 1
        rowStrings = [''] * numRows

        for char in s:
            rowStrings[rowIndex] += char
            if rowIndex == 0:
                dx = 1
            elif rowIndex == numRows - 1:
                dx = -1
            rowIndex += dx

        return ''.join(rowStrings)