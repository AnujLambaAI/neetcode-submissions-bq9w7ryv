class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False


        count1, count2 = {}, {} 
        for i in range(len(s1)):
            count1[s1[i]] = 1 + count1.get(s1[i],0)


        have, need = 0 , len(count1)
        l = 0
        for r in range(len(s2)):
            count2[s2[r]] = 1 + count2.get(s2[r], 0)
            if s2[r] in count1 and count2[s2[r]] == count1[s2[r]]:
                have += 1

            if (r-l+1) > len(s1):
                if s2[l] in count1 and count2[s2[l]]  == count1[s2[l]]:
                    have -= 1
                count2[s2[l]] -= 1
                l += 1
            if have == need:
                return True
        return False
