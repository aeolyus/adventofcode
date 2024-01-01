lines = open("input").read().splitlines()
points = []
for line in lines:
    x = int(line[:line.index(",")])
    y = int(line[line.index(",") + 2:])
    points.append([x, y])

region = 0
max = 10000//len(lines)
def mdist(L1, L2):
    return abs(L1[0] - L2[0]) + abs(L1[1] - L2[1])
for i in range(-max, max + 400):
    for j in range(-max, max + 400):
        currP = [i, j]
        d = 0
        for p in points:
            d += mdist(p, currP)
        if d < 10000:
            region +=1
print(region)
