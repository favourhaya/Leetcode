class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        visited = {}
        mx = 0
        l = 0
        t =0

        if len(nums) < k:
            return 0

        for r in range(len(nums)):
            if r-l == k:     
                visited[nums[l]] -= 1
                t -= nums[l]

                if visited[nums[l]] == 0:
                    visited.pop(nums[l])
                l +=1

            visited[nums[r]] = 1 + visited.get(nums[r],0)
            t += nums[r]

 
            
            if len(visited) == k and t >mx:
                mx = t 
           
        

           

        return mx
            
        