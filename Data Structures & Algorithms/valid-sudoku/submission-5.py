class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                k = board[r][c]
                if k == ".":
                    continue
                if k in rows[r] or k in cols[c] or k in squares[(r//3,c//3)]:
                    return False
                rows[r].add(k)
                cols[c].add(k)
                squares[(r//3,c//3)].add(k)
            
        return True

        

        

        