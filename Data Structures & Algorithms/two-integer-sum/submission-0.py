class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hM = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hM:
                return [hM[diff], i]
            hM[n] = i