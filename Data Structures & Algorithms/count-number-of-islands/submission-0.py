class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        islands = 0

        def dfs(r,c):
            stack = [(r,c)]
            visit.add((r,c))
            while stack:
                row, col = stack.pop()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (min(nr,nc) >= 0 and nr < rows and nc < cols and
                        grid[nr][nc] == "1" and (nr, nc) not in visit):
                        visit.add((nr,nc))
                        stack.append((nr,nc))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    visit.add((r,c))
                    dfs(r,c)
                    islands += 1
        return islands