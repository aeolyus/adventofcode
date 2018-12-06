lines = open("input").read().splitlines()
points = []
for line in lines:
    x = int(line[:line.index(",")])
    y = int(line[line.index(",") + 2:])
    points.append([x, y])

closest = [0 for i in range(len(lines))]
inf = [0 for i in range(len(lines))]

def mdist(L1, L2):
    return abs(L1[0] - L2[0])+abs(L1[1]-L2[1])
def find_closest(start, end, lst):
    for i in range(start, end):
        for j in range(start, end):
            currP = [i, j]
            index = 0
            min_d = mdist(currP, points[0])
            shouldAdd = True
            for id, point in enumerate(points[1:]):
                k = mdist(currP, point)
                if k == min_d:
                    shouldAdd = False
                if k < min_d:
                    index = id
                    min_d = k
                    shouldAdd = True
            if shouldAdd:
                lst[index] += 1

find_closest(-400, 800, closest)
find_closest(-401, 801, inf)
res = sorted([inf[i] for i in range(len(lines)) if inf[i] == closest[i] and inf[i] != 0], reverse = True)
print(res[0])
