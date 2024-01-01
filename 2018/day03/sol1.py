import collections

with open('input') as f:
    lines = f.readlines()
    arr = [[0 for i in range(1000)] for j in range(1000)]
    for line in lines:
        for i in range(int(line[line.find("@") + 2 : line.find(",")]), int(line[line.find("@") + 2 : line.find(",")]) + int(line[line.find(":") + 2 : line.find("x")])):
            for j in range(int(line[line.find(",") + 1 : line.find(":")]), int(line[line.find(",") + 1 : line.find(":")]) + int(line[line.find("x") + 1 :])):
                arr[i][j] += 1
    count = 0
    for a in arr:
        for j in a:
            if j > 1:
                count+=1
    print(count)
