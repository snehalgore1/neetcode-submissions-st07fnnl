class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        rowlen = len(grid)
        collen = len(grid[0])
        visited = set()
        print(rowlen)
        print(collen)
        for r in range(0,rowlen):
            for c in range(0,collen):
                if grid[r][c]=="0":
                    continue
                if grid[r][c]=="1" and (r,c) in visited:
                    continue
                if grid[r][c]=="1" and not (r,c) in visited:
                    count+=1
                    self.bfs(r,c,grid,visited)
        return count 

    def bfs(self,r,c,grid,visited):
        visited.add((r,c))
        neigh = [[0,1],[1,0],[0,-1],[-1,0]]
        l = [[r,c]]
        while l:
            for i in neigh:
                r1 = i[0]+l[0][0]
                c1 = i[1]+l[0][1]

                if r1 < 0 or r1>len(grid)-1:
                    continue
                
                if c1<0 or c1>len(grid[0])-1:
                    continue

                if grid[r1][c1] == "1" and not (r1,c1) in visited:
                    l.append([r1,c1])
                    visited.add((r1,c1))
            l.pop(0)