class Solution(object):
    @staticmethod
    def isIsomorphic(s, t):
        charIntMaps = [{}, {}]
        for i in range(len(s)):
            if s[i] not in charIntMaps[0].keys():
                charIntMaps[0][s[i]] = i

            sVal = charIntMaps[0][s[i]]

            if t[i] not in charIntMaps[1].keys():
                charIntMaps[1][t[i]] = i

            tVal = charIntMaps[1][t[i]]

            if sVal == tVal: continue

            else: return False

        return True