import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write

# code goes here
cnt = 0
crates = []
new = []
while True:
    inp = input().strip('\n')
    if not inp:
        cnt += 1
        if cnt == 1:
            n = len(crates[0])
            for i in range(n):
                curr= []
                for j in range(len(crates)-1):
                    if crates[j][i].strip():
                        curr.append(crates[j][i].strip())
                curr = curr[::-1]
                new.append(curr)
        if cnt == 2: break
        continue
    if cnt == 0:
        ln = len(inp)
        ln += 1
        ln //= 4
        curr = []
        for i in range(ln):
            curr.append(inp[i*4:i*4+4])
        crates.append(curr)
    else:
        inp = inp.split()
        n,x,y = int(inp[1]), int(inp[3]), int(inp[5])
        x-=1
        y-=1
        #print(new[x])

        #print(new[y])
        for i in range(len(new[x])-n, len(new[x])):
            new[y].append(new[x][i])
        for i in range(n):
            new[x].pop(-1)
        #print(new[x])

        #print(new[y])
res = ''.join([i[-1][1] for i in new])
print(res)



fin.close()
fout.close()
