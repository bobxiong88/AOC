import sys
from collections import deque
from itertools import permutations
stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write

#code goes here

cubes = []
while True:
    line = input().strip('\n')
    #print(line)
    if not line: break
    cubes.append(list(map(int,line.split(','))))
    
n = len(cubes)
mx = 25
vis = [False]*n
ans = 0
big = [[[False]*mx for i in range(mx)] for j in range(mx)]
for x,y,z in cubes:
    big[x][y][z] = True
queue = deque([[20,20,20]])
while queue:
    k = queue.popleft()
    x,y,z = k
    if big[x][y][z]:continue
    big[x][y][z] = True
    for a,b in [(0,1),(0,-1),(1,1),(1,-1),(2,1),(2,-1)]:
        bruh = k[:]
        bruh[a]+=b
        c,d,e = bruh
        if (-2<=c<mx) and (-2<=d<mx) and (-2<=e<mx):
            if not big[c][d][e]:
                queue.append([c,d,e])
def bfs(i):
    global ans
    queue = deque([i])
    while queue:
        i = queue.popleft()
        if vis[i]:break
        cords = cubes[i]
        vis[i] = True
        

for cords in cubes:
    for a,b in [(0,1),(0,-1),(1,1),(1,-1),(2,1),(2,-1)]:
        cp=cords[:]
        cp[a] += b
        #print(cords,cp)
        if cp in cubes:
            queue.append(cubes.index(cp))
        else:
            ans += 1
            x,y,z = cp
            if not big[x][y][z]:ans-=1
print(ans)




fin.close()
fout.close()
