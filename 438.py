class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pDict = {}
        sDict = {}
        res = []

        if len(p) > len(s):
            return[]
        for x in p:
            pDict[x] = 1 + pDict.get(x,0)

        left = 0
        print(len(p))

        for right in range(len(s)):

            if sDict == pDict:
                res.append(left)
                print("ok")
            
            
            print(sDict)
            if right - left >= len(p):
                sDict[s[left]] -= 1
                if sDict[s[left]] == 0:
                    sDict.pop(s[left])
                left += 1
                
            
            sDict[s[right]] = 1+ sDict.get(s[right],0)


        if sDict == pDict:
                res.append(left)
                print("ok")
            
        return res