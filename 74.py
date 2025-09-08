class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS =len(matrix),len(matrix[0])
        bot = ROWS-1
        top = 0
        ans = 0

        while top <= bot :
            row = (bot +top) //2
            if matrix[row][-1] < target:
                top = row +1
            elif matrix[row][0] >target:
                bot = row -1
            else:
                break

        if not top <= bot:
            return False
        row = (top +bot) //2
        
        l = 0
        r = COLS -1
        while l <= r:
            m = (l + r) //2
            if matrix[row][m] > target:
                r = m -1
            elif matrix[row][m] < target:
                l = m +1
            else:
                return True
        return False