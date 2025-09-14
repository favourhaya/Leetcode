class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals =  sorted(intervals, key = lambda x: x[0])
        print(intervals)

        seen = {}
        ans = []
       
        for n in intervals:
            old = None
            new = None
            adds = []
            for arg in seen:
                if (n[0] <= arg):
                    print("ok")
                    old = arg
                    if seen[arg] != False:
                        new = [min(n[0], seen[arg][0]), max(n[1], arg)]
            
                    seen[old] =False
                    if new:
                        adds.append(new)
           
            for li in adds:
                print(adds)
                seen[li[1]] = li

            if not old and not new:
                seen[n[1]] = n
        print(seen)
        for x,v in seen.items():
            if v != False:
                ans.append(v)
        return ans
        
        