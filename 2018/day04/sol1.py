with open('input') as f:
    lines = f.readlines()
    lines.sort()
    lst = [0 for i in range(9999)]
    start = 0
    guard = 0
    for line in lines:
        first = line[line.find("]") + 2]
        time = int(line[line.find(":") + 1: line.find(":") + 3])
        if (first == "G"):
            guard = int(line[line.find("d") + 3:line.find("b")])
        elif (first == "f"):
            start = time
        elif (first == "w"):
            slept = time - start
            lst[guard] += slept

    sleepyboi = lst.index(max(lst))

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
    print(sleepyboi * arr[sleepyboi].index(max(arr[sleepyboi])))
