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
    
# Another solution (optimized version of first solution)
class Solution(object):
    @staticmethod
    def isIsomorphic(s, t):
        charMap = {}
        used = set()
        for i in range(len(s)):
            if s[i] in charMap:
                if charMap[s[i]] != t[i]: return False

            else: 
                if t[i] not in used:
                    charMap[s[i]] = t[i]
                    used.add(t[i])

                else: return False

        return True