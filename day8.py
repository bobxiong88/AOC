import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write

# code goes here
grid = []
while True:
    inp = input().strip('\n')
    if inp == "": break
    grid.append(list(map(int,list(inp))))
n = len(grid)
m = len(grid[0])
res = (n+m)*4-4
pos = [[False for i in range(m)] for j in range(n)]
res = 0
for i in range(1,n-1):
    for j in range(1,m-1):
        left = 0
        for k in range(j-1, -1, -1):
            left += 1
            if grid[i][k] >= grid[i][j]:
                break
        right = 0
        for k in range(j+1,m):
            right += 1
            if grid[i][k] >= grid[i][j]:
                break
        up = 0
        for k in range(i-1, -1, -1):
            up += 1
            if grid[k][j] >= grid[i][j]:
                break
        down = 0
        for k in range(i+1,n):
            down += 1
            if grid[k][j] >= grid[i][j]:
                break
        res = max(res, left*up*right*down)

print(res)



fin.close()
fout.close()
