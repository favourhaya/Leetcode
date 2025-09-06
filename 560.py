class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pre = []
        curr = 0
        c = 0
        checked = {}
        for n in nums:

            curr += n
            pre.append(curr)

        i = 0
        while i< len(pre):
            arg = pre[i] - k
            if pre[i] == k:
                c +=1
            if arg in checked:
                print(pre[i])
                c+= checked[arg]

            checked[pre[i]] = 1 + checked.get(pre[i],0)
            i+=1
                
        print(checked)
        return c

        