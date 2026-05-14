class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        uniqChr = set()
        res = 0
        l = 0
        for r in range(len(s)):
            while s[r] in uniqChr:
                uniqChr.remove(s[l])
                l += 1
            uniqChr.add(s[r])
            res = max(res, (r-l+1))
        return res