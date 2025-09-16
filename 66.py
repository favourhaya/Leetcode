class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = [str(x) for x in digits]
        x = ''.join(ans)
        print(str(x[0]))
        x = str(int(x) + 1)
        output = []
        i = 0

        #print(li)
        while i < len(x):
            output.append(int(x[i]))
            i +=1
        return output
        