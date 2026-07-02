class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        countT, window = {}, {}
        for c in s1:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        l = 0
        for r in range(len(s2)):
            window[s2[r]] = 1 + window.get(s2[r], 0)
            if s2[r] in countT and window[s2[r]] == countT[s2[r]]:
                have += 1
                
            if (r-l+1) > len(s1):
                if s2[l] in countT and window[s2[l]] == countT[s2[l]]:
                    have -= 1
                window[s2[l]] -= 1
                l += 1
                
            if have == need:
                return True
        return False

            
         