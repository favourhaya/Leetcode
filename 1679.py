class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) -1
        c = 0
        checked = {}
        for num in nums:
            checked[num] = 1 + checked.get(num,0)
        print(checked)
        nums = sorted(nums)

        while l < r:
            s = nums[l] + nums[r]
            if s > k:
                #checked[nums[r]] -= 1
                r -= 1
               # checked[nums[r]] -= 1
            elif s<k:
                #checked[nums[l]] -= 1
                l +=1
             #   checked[nums[l]] -= 1
            elif s == k and checked[nums[l]] >0 and checked[nums[r]]> 0 and l !=r:
                c += 1
                print(checked, l ,r)
                checked[nums[l]] -= 1
                checked[nums[r]] -= 1
               
            else:
                if checked[nums[l]] == 0:
                  
                    l += 1
                    
                else:
                    
                    r -= 1

            print(checked)
        return c

      