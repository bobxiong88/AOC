import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write

# code goes here
num = dict()
while True:
    line = input().strip('\n')
    if not line:break
    line = line.split()
    x = line[0][:4]
    num[x] = line[1:]
def dfs(x):
    if x == "humn": return "x"
    if num[x][0].isdigit():
        return num[x][0]
    get = "("+str(dfs(num[x][0]))+num[x][1]+str(dfs(num[x][2]))+")"
    if "x" in get:
        return get
    else:
        return eval(get)
l = 0
r = 1000000000000000000
ex = dfs(num["root"][0])
a = dfs(num["root"][2])
for i in range(100):
    m = (l+r)/2
    k = ex.replace("x",str(m))
    k = eval(k)
    if k > a:
        l = m
    else:
        r = m
print(l,r)



fin.close()
fout.close()
