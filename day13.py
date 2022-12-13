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
from functools import cmp_to_key
def comp(l,r):
    #print(l,r)
    if type(l)==int and type(r)==int:
        if l < r: return 1
        elif l > r: return 0
        else: return 2
    if type(l) == list and type(r) == list:
        if len(l) == 0 and len(r) == 0: return 2
        if len(l) == 0: return 1
        if len(r) == 0: return 0
        k = comp(l[0],r[0])
        if k == 2:
            return comp(l[1:],r[1:])
        else:
            return k
    else:
        if type(l) == int:
            return comp([l],r)
        else:
            return comp(l,[r])
def compcomp(l,r):
    return comp(l,r)-1
    
prev = '0'
cnt = 0
mine = [[[2]],
[[6]]]
i = 0
while True:
    line = input().strip('\n')
    if not line:
        if not prev: break
        prev = line
    else: mine.append(eval(line))
    prev = line
mine = list(reversed(sorted(mine,  key=cmp_to_key(compcomp))))
print((mine.index([[2]])+1)*(1+mine.index([[6]])))
    




fin.close()
fout.close()
