class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]


        def is_valid(row, col):
             # Check column above
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            
            # Check upper-left diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            # Check upper-right diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1
            return True

        def backtrack(row):
            if row == n:
                result.append(["".join(r) for r in board])
            
            for col in range(n):
                if not is_valid(row, col):
                    continue
                
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."
            
        backtrack(0)
        return result