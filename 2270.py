class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        pre = []
        curr = 0
        c = 0
        for n in nums:
            curr +=n
            pre.append(curr)
        
        i = 0
        print(pre)
        while i < len(pre)-1:
            #print(x)
            if pre[i] >= pre[-1] - pre[i]:
                c += 1
            i += 1
        return c


            