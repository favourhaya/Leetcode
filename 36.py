class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        x = {}
        y = {}
        squares = {}
        for row in range(len(board)):
            for cell in range(len(board[row])):
                if board[row][cell] != ".":
                    if board[row][cell] not in x:
                        x[ board[row][cell]] = set()
                        x[board[row][cell]].add(cell)

                        y[board[row][cell]] = set()
                        y[board[row][cell]].add(row)

                        squares[board[row][cell]] = set()
                        squares[board[row][cell]].add((row//3 , cell // 3))
                    else:
                        if cell in x[board[row][cell]] or row in y[board[row][cell]] or (row//3 , cell // 3) in squares[board[row][cell]]:
                            return False           
                        x[board[row][cell]].add(cell)
                        y[board[row][cell]].add(row)
                        squares[board[row][cell]].add((row//3 , cell // 3))
                        
        print(x)
        return True
       
        