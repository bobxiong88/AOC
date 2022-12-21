import sys

stdprint = print
stdinput = input

#'''
fin = open("in.txt")
fout = open("out.txt", "w")
#'''

input = fin.readline
#print = fout.write

# code goes here
a = []
while True:
    line = input().strip('\n')
    if not line: break
    a.append(int(line))
n = len(a)
a = [i*811589153 for i in a]
b = [(i, a[i]) for i in range(n)]
for dd in range(10):
    for i in range(n):
        x=b.index((i,a[i]))
        b.remove((i,a[i]))
        b.insert((x+a[i])%(n-1),(i,a[i]))
    #print(b)
k=b.index((a.index(0),0))
print(b[(k+1000)%n][1]+b[(k+2000)%n][1]+b[(k+3000)%n][1])
#'''
fin.close()
fout.close()
#'''
