with open('input1') as f:
    lines = f.readlines()
    count = 0
    for l in lines:
        if l[0] == '+':
            count += int(l[1:])
        else:
            count -= int(l[1:])
    print(count)
