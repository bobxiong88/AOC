import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write


# code goes here
tot = 0
mp = {'X': 'A', 'Y': 'B', 'Z': 'C'}
score = {'A':1, 'B': 2, 'C': 3}
ls = ['A', 'B', 'C','A','B','C']
while True:
    inp = input().strip('\n')
    if not inp: break
    a,b = inp.split()
    i = ls.index(a)
    if b == 'Z':
        m = ls[i+1]
        tot += 6
        tot += score[m]
    elif b == 'Y':
        m = ls[i]
        tot += 3
        tot += score[m]
    else:
        m = ls[i+2]
        tot += 0
        tot += score[m]
    #stdprint(a,b,m)
print(str(tot))
stdprint(tot)
fin.close()
fout.close()
