class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        l = 0
        m = 0
        r = len(nums) - 1
        nums = sorted(nums)
        while l < r:
            arg = nums[l] + nums[r]
            if arg > m:
                m =arg
            l += 1
            r -= 1
        return m
        