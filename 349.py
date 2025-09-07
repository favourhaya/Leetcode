class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 ={}
        res = []
        for x in nums1:
            n1[x] = 1
        #print(n1)

        n2 ={}
        for x in nums2:
            n2[x] = 1
        #print(n2)

        if len(n1) > len(n2):
            large = n1
            small = n2
        else:
            large = n2
            small = n2
        
        for x in large:
            if x in n2 and x in n1:
                res.append(x)
        return res