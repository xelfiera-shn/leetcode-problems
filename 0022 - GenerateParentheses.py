class Solution(object):
    @staticmethod
    def generateParenthesis(n):
        validCombinations = []
        addNewParenthes(validCombinations, '(', 1, 0, n)

        return validCombinations

def addNewParenthes(validCombinations, template, open, closed, n):
    if len(template) == n * 2:
        validCombinations.append(template)
        return
    
    if open < n:
        addNewParenthes(validCombinations, template + '(', open + 1, closed, n)

    if open > closed:
        addNewParenthes(validCombinations, template + ')', open, closed + 1, n)

'''

            '('
            /  \
         '(('  '()'
         /  \     \
     '((('  '(()' '()('

'''