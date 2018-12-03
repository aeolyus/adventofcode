with open('input') as f:
    lines = f.readlines()
    arr = [[0 for i in range(1000)] for j in range(1000)]
    there = set()
    for line in lines:
        id = int(line[1:line.find("@") - 1])
        for i in range(int(line[line.find("@") + 2 : line.find(",")]), int(line[line.find("@") + 2 : line.find(",")]) + int(line[line.find(":") + 2 : line.find("x")])):
            for j in range(int(line[line.find(",") + 1 : line.find(":")]), int(line[line.find(",") + 1 : line.find(":")]) + int(line[line.find("x") + 1 :])):
                if arr[i][j] != 0:
                    there.add(arr[i][j])
                    there.add(id)
                arr[i][j] = id
    print([i for i in range(1, len(lines) + 1) if i not in there][0])
