import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write

# code goes here
while True:
    inp = input().strip('\n')
    if not inp: break
    #stdprint(a,b,m)



fin.close()
fout.close()
