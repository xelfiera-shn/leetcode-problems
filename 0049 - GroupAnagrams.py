class Solution(object):
    @staticmethod
    def groupAnagrams(strs):
        anagramGroups = {}

        for string in strs:
            stringTuple = tuple(sorted(string))

            if stringTuple not in anagramGroups:
                anagramGroups[stringTuple] = []

            anagramGroups[stringTuple].append(string)

        return list(anagramGroups.values())