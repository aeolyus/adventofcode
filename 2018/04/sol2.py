with open('input') as f:
    lines = f.readlines()
    lines.sort()
    start = 0
    guard = 0
    arr = [[0 for i in range(100)] for i in range(9999)]
    for line in lines:
        first = line[line.find("]") + 2]
        time = int(line[line.find(":") + 1: line.find(":") + 3])
        if (first == "G"):
            guard = int(line[line.find("d") + 3:line.find("b")])
        elif (first == "f"):
            start = time
        elif (first == "w"):
            for i in range(start, time):
                arr[guard][i] += 1
    res = max([[i, max(arr[i])] for i in range(9999) if max(arr[i]) != 0], key = lambda a : a[1])
    print(res[0] * arr[res[0]].index(res[1]))
