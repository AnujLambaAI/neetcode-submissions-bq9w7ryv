class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenval = set()
        for num in nums:
            if num in seenval:
                return True
            seenval.add(num)
        return False
      