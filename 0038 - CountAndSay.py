class Solution(object):
    @staticmethod
    def countAndSay(n):
        runLengthEncodes = ['1']

        for i in range(1, n):
            previousMember = runLengthEncodes[i - 1]

            index = 0
            currentMember = ''
            while index < len(previousMember):
                previousChar = list(previousMember)[index]
                previousCharCount = 0

                while index < len(previousMember) and list(previousMember)[index] == previousChar:
                    index += 1
                    previousCharCount += 1

                currentMember += str(previousCharCount)
                currentMember += previousChar

            runLengthEncodes.append(currentMember)

        return runLengthEncodes[-1]