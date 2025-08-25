class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer1 =0
        pointer2 = len(nums) -1
        c = 0



        for i in range(len(nums)):
            if nums[i] != val:
                nums[c] = nums[i]
                c+=1
            i += 1
        return c

            