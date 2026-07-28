class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows , cols = len(grid) , len(grid[0])
        visit = set()
        directions = [(1,0),(-1, 0 ), (0, 1),(0,-1)]

        def dfs(r,c):
            stack = [(r,c)]
            visit.add((r,c))
            area = 0
            while stack:
                row, col = stack.pop()
                area += 1
                for dr, dc in directions:
                    nr, nc = row + dr, col +dc
                    if (min(nr,nc) >=0 and nr < rows and nc <cols and
                        grid[nr][nc] == 1 and (nr,nc ) not in visit):
                        visit.add((nr,nc))
                        stack.append((nr,nc))
                        
            return area
        maxArea = 0
        for r in range(rows):
            for c in range(cols) :
                if grid[r][c] == 1 and (r,c) not in visit:
                    visit.add((r,c))
                    maxArea = max(maxArea, dfs(r,c))

        return maxArea      