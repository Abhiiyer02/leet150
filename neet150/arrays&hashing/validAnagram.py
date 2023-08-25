class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

        #s1 = set(s)
        # hash1 = {}
        # if(len(s) != len(t)):
        #     return False
        # for i in s1:
        #     hash1[i] = s.count(i)
        
        # for i in t :
        #     if i not in s1:
        #         return False
        #     if t.count(i) != hash1[i]:
        #         return False
        # return True