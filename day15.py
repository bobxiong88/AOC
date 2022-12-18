import sys

stdprint = print
stdinput = input



#input = fin.readline
#print = fout.write

# code goes here

inp = """Sensor at x=2692921, y=2988627: closest beacon is at x=2453611, y=3029623
Sensor at x=1557973, y=1620482: closest beacon is at x=1908435, y=2403457
Sensor at x=278431, y=3878878: closest beacon is at x=-1050422, y=3218536
Sensor at x=1432037, y=3317707: closest beacon is at x=2453611, y=3029623
Sensor at x=3191434, y=3564121: closest beacon is at x=3420256, y=2939344
Sensor at x=3080887, y=2781756: closest beacon is at x=3420256, y=2939344
Sensor at x=3543287, y=3060807: closest beacon is at x=3420256, y=2939344
Sensor at x=2476158, y=3949016: closest beacon is at x=2453611, y=3029623
Sensor at x=3999769, y=3985671: closest beacon is at x=3420256, y=2939344
Sensor at x=2435331, y=2200565: closest beacon is at x=1908435, y=2403457
Sensor at x=3970047, y=2036397: closest beacon is at x=3691788, y=1874066
Sensor at x=2232167, y=2750817: closest beacon is at x=2453611, y=3029623
Sensor at x=157988, y=333826: closest beacon is at x=-1236383, y=477990
Sensor at x=1035254, y=2261267: closest beacon is at x=1908435, y=2403457
Sensor at x=1154009, y=888885: closest beacon is at x=1070922, y=-543463
Sensor at x=2704724, y=257848: closest beacon is at x=3428489, y=-741777
Sensor at x=3672526, y=2651153: closest beacon is at x=3420256, y=2939344
Sensor at x=2030614, y=2603134: closest beacon is at x=1908435, y=2403457
Sensor at x=2550448, y=2781018: closest beacon is at x=2453611, y=3029623
Sensor at x=3162759, y=2196461: closest beacon is at x=3691788, y=1874066
Sensor at x=463834, y=1709480: closest beacon is at x=-208427, y=2000000
Sensor at x=217427, y=2725325: closest beacon is at x=-208427, y=2000000
Sensor at x=3903198, y=945190: closest beacon is at x=3691788, y=1874066

"""

pnts = []
mx=4000000
def check(x,y):
    for sx,sy,d in pnts:
        if abs(sx-x)+abs(sy-y) <= d:
            return False
    return True
for line in inp.split('\n'):
    if not line:break
    cur = 0
    res = []
    for i in range(4):
        k = line[cur:].index('=')+1+cur
        cur = k
        pos = ''
        while k<len(line) and (line[k].isdigit() or line[k]=='-'):
            pos = pos+line[k]
            k += 1
        res.append(int(pos))
    sx,sy,bx,by = res
    d = abs(sx-bx)+abs(sy-by)
    pnts.append((sx,sy,d))

for sx,sy,d in pnts:
    dr = [[1,-1],[-1,-1],[-1,1],[1,1]]
    x = sx+d+1
    y = sy
    for i in range(4):
        for j in range(d+1):
            a,b = dr[i]
            if x in range(0,mx+1) and y in range(0,mx+1) and check(x,y):
                print(x*4000000+y)
                print(x,y)
                sys.exit(0)
            x = x+a
            y = y+b

