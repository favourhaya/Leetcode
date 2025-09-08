class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r =  max(piles)
        res = r

        while l <= r:
            m = (l+ r) //2
            amount = 0
            for p in piles:
                if p % m ==0:
                    amount += (p // m)
                else:
                    amount +=(p // m) +1
            #print(amount,m)
            if amount <= h:
                res = min(res,m)
                r = m-1
            else:
                l = m+1
        return res
            
    