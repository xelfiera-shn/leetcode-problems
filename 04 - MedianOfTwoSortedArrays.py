class Solution(object):
    @staticmethod
    def findMedianSortedArrays(nums1, nums2):
        sortedArray = sorted(nums1 + nums2)
        medianIndex = int(len(sortedArray) / 2)
        if len(sortedArray) % 2 == 0:
            return (float(sortedArray[medianIndex - 1]) + float(sortedArray[medianIndex])) / 2
        
        else:
            return sortedArray[medianIndex]