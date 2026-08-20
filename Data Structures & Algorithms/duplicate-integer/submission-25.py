class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        alrhave = set()
        for num in nums:
            if num in alrhave:
                return True
            alrhave.add(num)
        return False