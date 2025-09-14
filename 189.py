class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        rev = nums[::-1]
        k = k% len(nums)
        print(k)
        nums[0:k] = rev[0:k][::-1]
        nums[k:] = rev[k:][::-1]


        