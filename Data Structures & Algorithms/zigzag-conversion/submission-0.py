class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = [""] * numRows
        curRow = 0
        direction = 1
        for c in s:
            rows[curRow] += c
            curRow += direction


            if curRow == (numRows - 1) or curRow == 0:
                direction = -direction
           
            
        
        return "".join(rows)
            
