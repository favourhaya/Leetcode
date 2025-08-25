import math 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prod = nums[0]
        prod2 = 1
        
        for n in range(1, len(nums)):
            res[n] = prod
            prod = prod * nums[n]
           


        for n in range( len(nums) -1,-1,-1):
            res[n] *= prod2
            prod2 *= nums[n]
        return res
