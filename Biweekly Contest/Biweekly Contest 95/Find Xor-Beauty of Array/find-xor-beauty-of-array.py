class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res
