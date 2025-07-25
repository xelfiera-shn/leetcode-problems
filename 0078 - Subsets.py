class Solution(object):
    @staticmethod
    def subsets(nums):
        result = []
        candidate = []

        def backtrack(start, k):
            if len(candidate) == k:
                result.append(candidate[ : ])
                return
            
            for index in range(start, len(nums)):
                candidate.append(nums[index])
                backtrack(index + 1, k)
                candidate.pop()

        for i in range(len(nums) + 1):
            backtrack(0, i)

        return result
    
# Common solution on the web
class Solution(object):
    @staticmethod
    def subsets(nums):
        def backtrack(start, path):
            result.append(path[ : ])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        result = []
        backtrack(0, [])

        return result