class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        checked= {}
        l = 0
        vowels = ["a","e","i","o","u"]
        count= 0
        mx=0

        for r in range(len(s)):
            if r -l == k:
                if s[l] in checked:
                    
                    checked[s[l]] -= 1
                    count -= 1
                    if  checked[s[l]] == 0 :
                        checked.pop(s[l])
                l +=  1
            
            if s[r] in vowels:
                checked[s[r]] = 1 + checked.get(s[r], 0 )
                count += 1
            if count > mx:
                mx =  count
            
        return mx   