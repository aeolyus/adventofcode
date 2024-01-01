from blist import blist
inp = open("input").read().split()

players =[0 for i in range(int(inp[0]))]
marbles = int(inp[6]) * 100
circle = blist([0])
m = 0
p = -1
index = 0
while (m < marbles):
    p = (p + 1) % len(players)
    m += 1
    if (m % 23 == 0):
        index = (index - 6) % len(circle)
        players[p] += m + circle.pop(index)
        index -= 1
    else:
        index = (index + 2) % len(circle)
        circle.insert(index + 1, m)
print(max(players))
