class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l = 0
        r= 0
        while r < len(word):
            if word[r] == ch:
                #word[l] = word[r] 
                newword = word[l:r +1][::-1]
                return newword + word[r+1:]
            else:
                r+=1
        return word