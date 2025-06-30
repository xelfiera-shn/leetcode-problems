class Solution(object):
    @staticmethod
    def plusOne(digits):
        index = len(digits) - 1
        digits[index] += 1
        for i in range(len(digits)):
            if digits[index] / 10 > 0:
                if index != 0: digits[index - 1] += 1

                else:
                    digits.insert(0, 1)
                    index += 1

                digits[index] = digits[index] % 10

            else: break

            index -= 1

        return digits