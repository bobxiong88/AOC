import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write

# code goes here
X = 1
cycle = 1
ans = 0
screen = [['#']*40 for i in range(6)]
while True:
    line = input().strip('\n')
    if not line: break
    if line[0] == 'n':
        V = 0
        k = 1
    else:
        _, V = line.split()
        V = int(V)
        k = 2
    for i in range(k):
        x = (cycle-1)%40
        y = (cycle-1)//40
        if  X-1 <= x <= X+1:
            screen[y][x] = "#"
        else:
            screen[y][x] = "."
        cycle += 1
    X += V
for i in screen:
    print(''.join(i))




fin.close()
fout.close()
