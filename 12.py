class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        vals = {
            'M':1000,
            'CM':900,
            'D':500,
            'CD':400,
            'C':100,
            'XC':90,
            'L':50,
            'XL':40,
            'X':10,
            'IX':9,
            "V":5,
            'IV':4,
            "I": 1
        }

        for n in vals:
            if num // vals[n] > 0:
                count = num // vals[n]
                output += ( n *count)

                num = num % vals[n]
               
               
        return output


