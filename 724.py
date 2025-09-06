class NumArray:

    def __init__(self, nums: List[int]):
        self.pre = []
        curr = 0
        for n in nums:
            curr += n
            self.pre.append(curr)


    def sumRange(self, left: int, right: int) -> int:
        r = self.pre[right]

        if left > 0:
            l = self.pre[left -1]
        else:
            l = 0
        return r - l

        print(self.pre)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)