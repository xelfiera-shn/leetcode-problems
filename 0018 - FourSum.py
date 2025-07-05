class Solution(object):
    @staticmethod
    def fourSum(nums, target):
        nums.sort()
        quadruplets = []

        for xIndex in range(len(nums) - 1):
            yIndex = xIndex + 1
            zIndex = len(nums) - 2
            tIndex = len(nums) - 1

            while yIndex < tIndex:
                yIndex = xIndex + 1
                while yIndex < zIndex:
                    candidate = [nums[xIndex], nums[yIndex], nums[zIndex], nums[tIndex]]
                    sum = candidate[0] + candidate[1] + candidate[2] + candidate[3]

                    if sum == target:
                        if candidate not in quadruplets:
                            quadruplets.append(candidate)
                        zIndex -= 1

                    elif sum > target: zIndex -= 1

                    elif sum < target: yIndex += 1

                tIndex -= 1
                zIndex = tIndex - 1

        return quadruplets