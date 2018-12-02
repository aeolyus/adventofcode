with open('input') as f:
    lines = f.readlines()
    curr = 0
    lst = [0]
    found = False
    while (not found) :
        for l in lines:
            if l[0] == '+':
                curr += int(l[1:])
            else:
                curr -= int(l[1:])
            if curr in lst:
                print(curr)
                found = True
                break
            else:
                lst.append(curr)
