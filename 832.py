class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        li = []
        for row in image:
            w =[]
            for n in row:
                if n == 0:
                    w.append(1)
                else:
                    w.append(0)
            li.append(w[::-1])

        return li
           
        