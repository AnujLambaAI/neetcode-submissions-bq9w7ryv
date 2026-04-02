class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hM = set()
        for num in nums:
            if num in hM:
                return True
            hM.add(num)
        return False
        