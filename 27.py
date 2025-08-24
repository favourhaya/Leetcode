class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer1 =0
        pointer2 = len(nums) -1
        c = 0

        if len(nums) == 1:
            print("ASd")
            if nums[0] == val:
                print("asdf")
                del nums[0]

        mid = len(nums) // 2


        while pointer1  < mid or pointer2  > mid :

            if nums[pointer2] == val:
                pointer2 -= 1

            if nums[pointer1] == val:
                nums[pointer1],nums[pointer2] =  nums[pointer2],nums[pointer1]
                c+=1
            else:
                pointer1 += 1
        
        if c != 0:
            del nums[len(nums)-c-1:]
