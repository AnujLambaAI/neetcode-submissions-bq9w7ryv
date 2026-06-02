class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        

        countS , countT = {}, {}
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            countT[t[r]] = 1 + countT.get(t[r], 0)

        return countS == countT 