class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        checked = {}
        l = 0
        c = 0
        mx = 0
        t = 0

        if len(fruits) == 1:
            return 1

        for r in range(len(fruits)):
           
            if len(checked) >  2:
                checked[fruits[l]] -= 1 
                c-= 1
                if checked[fruits[l]] == 0:
                    checked.pop(fruits[l])
                l += 1

            checked[fruits[r]] = 1 + checked.get(fruits[r],0)
            if len(checked) <= 2:
                t =  sum(checked.values())
            print(t)
            if t > mx:
                mx = t
            
        return mx 
                     