
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = {}
        res= []
        for word in strs:
            key = "".join(sorted(word))
            if key not in output: 
                output[key] = [word]
            else:
                output[key].append(word) 

        for x in output.values():
            res.append(x)
        return res
