# The solution doesn't require storing 64-bit integers.
class Solution(object):
    @staticmethod
    def reverse(x):
        isNegative = True if x < 0 else False
        xString = str(abs(x))
        reversedString = xString[ : : -1]
        edgeValueString = str(pow(2, 31) if isNegative else pow(2, 31) - 1)

        if len(reversedString) == len(edgeValueString):
            for i in range(len(reversedString)):
                if int(reversedString[i]) > int(edgeValueString[i]):
                    return 0
                
                elif int(reversedString[i]) == int(edgeValueString[i]):
                    continue

                else:
                    break

        return -int(reversedString) if isNegative else int(reversedString)
    
# With storing 64-bit integers.
class Solution(object):
    @staticmethod
    def reverse(x):
        sign = -1 if x < 0 else 1
        reversedX = int(str(abs(x))[ : : -1])

        return sign * reversedX if -pow(2, 31) <= reversedX <= pow(2, 31) - 1 else 0