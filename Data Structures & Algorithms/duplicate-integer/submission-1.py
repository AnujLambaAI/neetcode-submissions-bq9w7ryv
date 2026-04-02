class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hM = {}
        for num in nums:
            if num in hM:
                return True
            hM[num] = 1
        return False
        

        