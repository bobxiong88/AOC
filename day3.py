import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write

# code goes here
lst = [chr(i+ord('a')) for i in range(26)]+[chr(i+ord('A')) for i in range(26)]
lst = [0]+lst
ans = 0
bags = []
while True:
    line = input().strip('\n')
    if not line: break
    bags.append(line)
n = len(bags)
for i in range(n//3):
    for x in bags[i*3]:
        if x in bags[i*3+1] and x in bags[i*3+2]:
            ans += lst.index(x)
            break
print(ans)



fin.close()
fout.close()
