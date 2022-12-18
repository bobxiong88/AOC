import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write

#code goes here
rocks = [
["####"],

[".#.", "###", ".#."],

["..#", "..#", "###",],

["#", "#", "#", "#"],

["##", "##"]]

jet = input().strip('\n')
k = 0
grid = [['#']*7]
for r in range(2022):
    rock = rocks[r%5]
    lx = len(rock[0])
    ly = len(rock)
    px,py = 2, ly-1
    grid = [['.']*7 for i in range(3)]+grid
    while True:
        for i in range(x):
            for j in range(y):
                if rock[i][j]
        

print(res)



fin.close()
fout.close()
