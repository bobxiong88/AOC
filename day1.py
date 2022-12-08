import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")


'''
input = fin.readline
print = fout.write
'''

# code goes here
prev = 1
elv = []
acc = 0
x = 1
while True:
    line = input().strip('\n')
    if line == '':
        if prev == '':
            break
        elv.append((acc, x))
        acc = 0
        x += 1
    else:
        acc += int(line)
    prev = line
elv.sort(reverse = True)
print(elv[0][0]+elv[1][0]+elv[2][0])

fin.close()
fout.close()
