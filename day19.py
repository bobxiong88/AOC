import sys

stdprint = print
stdinput = input


fin = open("in.txt")
fout = open("out.txt", "w")

input = fin.readline
#print = fout.write
inp = """Blueprint 1:Each ore robot costs 4 ore.Each clay robot costs 2 ore.Each obsidian robot costs 3 ore and 14 clay.Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2:Each ore robot costs 2 ore.Each clay robot costs 3 ore.Each obsidian robot costs 3 ore and 8 clay.Each geode robot costs 3 ore and 12 obsidian.

"""#code goes here
ans = 0
x = 1
for line in inp.split('\n'):
    if not line:break
    n = len(line)
    line = list(line)
    curr = ''
    nums = []
    for i in range(n):
        if line[i].isdigit():
            curr += line[i]
        else:
            if curr:
                nums.append(int(curr))
                curr = ''
    oreu = nums[1]
    clayu = nums[2]
    obsu = (nums[3],nums[4])
    geou = (nums[5],nums[6])
    #print(oreu,clayu,obsu,geou)
    res = 0
    def solve(i,j,k,l,ore,clay,obs,geo,orec,clayc,obsc,geoc,day):
        if day == 24:
            return geoc
        if day <= i:
            if orec >= oreu:
                return solve(i,j,k,l,ore+1,clay,obs,geo,orec+ore-oreu,clayc+clay,obsc+obs,geoc+geo,day+1)
            else:
                return solve(i,j,k,l,ore,clay,obs,geo,orec+ore,clayc+clay,obsc+obs,geoc+geo,day+1)
        elif i<day<=k:
            used = False
            res = 0
            if orec >= clayu:
                res=max(res, solve(i,j,k,l,ore,clay+1,obs,geo,orec+ore-clayu,clayc+clay,obsc+obs,geoc+geo,day+1))
                used = True
            if orec >= obsu[0] and clayc >= obsu[1]:
                res=max(res, solve(i,j,k,l,ore,clay,obs+1,geo,orec+ore-obsu[0],clayc+clay-obsu[1],obsc+obs,geoc+geo,day+1))
                used = True
            
            res = max(res,solve(i,j,k,l,ore,clay,obs,geo,orec+ore,clayc+clay,obsc+obs,geoc+geo,day+1))
            return res
        else:
            if orec >= geou[0] and obsc >= geou[1]:
                return solve(i,j,k,l,ore,clay,obs,geo+1,orec+ore-geou[0],clayc+clay,obsc+obs-geou[1],geoc+geo,day+1)
            else:
                return solve(i,j,k,l,ore,clay,obs,geo,orec+ore,clayc+clay,obsc+obs,geoc+geo,day+1)
        
    for i in range(24):
        for j in range(i+1,24):
            for k in range(j+1,24):
                for l in range(k+1,24):
                    res = max(res, solve(i,j,k,l,1,0,0,0,0,0,0,0,0))
    print(x,res)
    ans += x*res
    x+=1
print(ans)

fin.close()
fout.close()
