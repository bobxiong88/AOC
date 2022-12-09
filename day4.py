import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write

# code goes here
ans = 0
while True:
    line = input().strip('\n')
    if not line: break
    x,y = line.split(',')
    a,b = map(int, x.split('-'))
    c,d = map(int, y.split('-'))
    bruh = [0]*100
    for i in range(a,b+1):
        bruh[i]+=1
    for i in range(c,d+1):
        bruh[i]+=1
    ans += bruh.count(2)>=1
print(ans)



fin.close()
fout.close()
