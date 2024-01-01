f = open('input').readlines()

w1 = f[0].split(',')
w2 = f[1].split(',')

table = {}

sol1, sol2 = [], []

DX = {'R': 1, 'L': -1, 'U': 0, 'D': 0}
DY = {'R': 0, 'L': 0, 'U': 1, 'D': -1}

distance = 0
x, y = 0, 0
for inst in w1:
    direction = inst[0]
    length = int(inst[1:])
    for i in range(1, length + 1):
        distance += 1
        x += DX[direction]
        y += DY[direction]
        if (x,y) not in table:
            table[(x,y)] = distance

distance = 0
x, y = 0, 0
for inst in w2:
    direction = inst[0]
    length = int(inst[1:])
    for i in range(1, length + 1):
        distance += 1
        x += DX[direction]
        y += DY[direction]
        if (x,y) in table:
            sol1.append(abs(x) + abs(y))
            sol2.append(distance + table[(x,y)])
print(min(sol1))
print(min(sol2))
