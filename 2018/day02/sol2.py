with open('input') as f:
    lst = f.read().splitlines()
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            diff = set.difference(set(lst[i]), set(lst[j]))
            if len(diff) == 1:
                letter = diff.pop()
                res = [a for a in range(len(lst[i])) if lst[i][a] != lst[j][a]]
                if len(res) == 1:
                    print(lst[i].replace(lst[i][res[0]], ""))
