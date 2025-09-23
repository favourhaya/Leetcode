class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        output = {}
        for n in nums:
            output[n] =  1 + output.get(n,0)
        return min(output,key = lambda x: output[x])

        