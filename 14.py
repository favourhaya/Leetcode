class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""

        argument = set(strs[0][:1])
        prefix_len = 1
        longest = ""
        
        while prefix_len <= len(max(strs)):
            for st in strs:
                if st[:prefix_len] in argument:
                    continue
                else:
                    return longest
            longest = strs[0][:prefix_len]
            argument.remove(strs[0][:prefix_len])
            prefix_len += 1
            argument.add(strs[0][:prefix_len])
        return longest




        