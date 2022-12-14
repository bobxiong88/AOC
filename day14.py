import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write

# code goes here
# 0 False
# 1 True
# 2 Equal
mx = 2000
grid = [['.' for i in range(mx)] for j in range(mx)]
k = 0
while True:
    line = input().strip('\n')
    if not line: break
    line = line.split('->')
    path = [list(map(int, i.split(','))) for i in line]
    n = len(path)
    for i in range(n-1):
        x1,y1 = path[i]
        x2,y2 = path[i+1]
        k = max(k, y1,y2)
        if x1 == x2:
            for j in range(min(y1,y2),max(y1,y2)+1):
                grid[j][x1] = '#'
        else:
            for j in range(min(x1,x2),max(x1,x2)+1):
                grid[y1][j] = '#'
for i in range(mx):
    grid[k+2][i] = '#'
ans = 0
def fall(x,y):
    if grid[y+1][x] == '.':
        return fall(x,y+1)
    else:
        if grid[y+1][x-1] == '.':
            return fall(x-1,y+1)
        elif grid[y+1][x+1] == '.':
            return fall(x+1,y+1)
        else:
            grid[y][x] = 'o'
            if x == 500 and y == 0: return True

while True:
    ans += 1
    res = fall(500,0)
    if res:
        break

print(ans)


fin.close()
fout.close()
