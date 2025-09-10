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
    
# Another solution (recursive)
class Solution(object):
    @staticmethod
    def countAndSay(n):
        def buildMember(previousMember):
            currentMember = ''
            previousMember += '#'
            previousCharCount = 1

            for i in range(len(previousMember) - 1):
                if previousMember[i] == previousMember[i + 1]:
                    previousCharCount += 1
                    continue

                else:
                    currentMember += str(previousCharCount) + previousMember[i]
                    previousCharCount = 1

            return currentMember
        
        member = '1'
        for i in range(n - 1):
            member = buildMember(member)

        return member