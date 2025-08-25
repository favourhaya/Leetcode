class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for n in range(len(nums)):
            if n > 0  and nums[n] == nums[n-1]:
                continue
            left, right = n+1, len(nums)-1
            while left < right:
                Sum = nums[left] + nums[right] +nums[n]
                if Sum > 0:
                    right -= 1
                elif Sum < 0:
                    left +=1
                else:
                    res.append([nums[left] ,nums[right] ,nums[n]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left +=1
        return res
 
            
 