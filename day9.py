import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write

# code goes here
ans = 0
ins = []
while True:
    line = input().strip('\n')
    if not line:break
    a,b = line.split()
    ins.append((a,int(b)))
mx = 1000
grid = [[0]*mx for i in range(mx)]
kt = [[mx//2,mx//2] for i in range(10)]
grid[mx//2][mx//2] = 1
for d,k in ins:
    pos = [0,0]
    if d == 'U':
        pos[0] = -1
    if d == 'D':
        pos[0] = 1
    if d == 'L':
        pos[1] = -1
    if d == 'R':
        pos[1] = 1
    #print(d,k,pos)
    
    for i in range(k):
        kt[0] = [kt[0][0]+pos[0],kt[0][1]+pos[1]]
        for j in range(1,10):
            dx,dy = kt[j-1][0]-kt[j][0],kt[j-1][1]-kt[j][1]
            if abs(dx)<=1 and abs(dy)<=1:
                pass
            else:
                if abs(dx)>=2:
                    kt[j][0] += dx//2
                    kt[j][1] += dy//(1+(abs(dy)>=2))
                elif abs(dy)>=2:
                    kt[j][1] += dy//2
                    kt[j][0] += dx//(1+(abs(dx)>=2))
        grid[kt[9][0]][kt[9][1]] = 1

ans = 0
for i in range(mx):
    ans += sum(grid[i])
print(ans)



fin.close()
fout.close()
