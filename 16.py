class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = {}
        nums =  sorted(nums)
        m = []
        l = 0
        r =  len(nums) -1
        closest = float("inf")
        ansSum = 0
        for n in range(len(nums)):
            l = n +1
            r = len(nums) -1     
            target
            while l < r:
                Sum = nums[l] +nums[n]+ nums[r]
                ans = abs(target -Sum)
                if ans < closest:
                    closest =ans
                    ansSum =Sum
                if Sum > target:
                    r-=1
                elif Sum < target:
                    l+=1
                else:
                    return Sum
            l = 0 
            r= 0
        return ansSum
        
      