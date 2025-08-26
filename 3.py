class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        unique = []

        res = [0]

        if s == " ":
            return 1

        for right in range(len(s)):
            
            if s[right] in unique:
                unique = unique[unique.index(s[right]) +1:]
                unique.append(s[right])
 
            else:
                unique.append(s[right])
            res.append(len(unique))


        
        return max(res)
        