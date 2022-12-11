import sys


# code goes here
in1 = [
[[79,98],
 [1, 19],
 [23, 2, 3]],
[[54, 65, 75, 74],
 [0, 6],
 [19, 2, 0]],
[[79,60,97],
 [3, 0],
 [13, 1, 3]],
[[74],
 [0, 3],
 [17, 0, 1]]]

in2 = [
[[83, 88, 96, 79, 86, 88, 70],
[1, 5],
[11, 2, 3]],
[[59, 63, 98, 85, 68, 72],
 [1, 11],
 [5, 4, 0]],
[[90, 79, 97, 52, 90, 94, 71, 70],
 [0, 2],
 [19, 5, 6]],
[[97, 55, 62],
 [0, 5],
 [13, 2, 6]],
[[74, 54, 94, 76],
 [3, 0],
 [7,0,3]],
[[58],
 [0, 4],
 [17, 7, 1]],
[[66, 63],
 [0, 6],
 [2, 7, 5]],
[[56, 56, 90, 96, 68],
 [0, 7],
 [3, 4, 1]]
    ]
monk = in1
n = len(monk)
cnt = [0]*len(monk)
lcm = 1
for i in range(n):
    lcm *= monk[i][2][0]
for i in range(10000):
    n = len(monk)
    for x in range(n):
        items = monk[x][0]
        op = monk[x][1]
        rule = monk[x][2]
        for item in items:
            if op[0] == 0:
                item = item+op[1]
            elif op[0] == 1:
                item = item*op[1]
            else:
                item = item*item
            item %= lcm
            #print(item)
            if item%rule[0]==0:
                monk[rule[1]][0].append(item)
            else:
                monk[rule[2]][0].append(item)
            cnt[x]+=1
        monk[x][0] = []
        
    #print(monk[0][0],monk[1][0],monk[2][0])
res = sorted(cnt)
print(res[-1]*res[-2])
        
