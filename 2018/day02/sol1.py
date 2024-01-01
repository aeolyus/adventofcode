import collections

with open('input') as f:
    lines = f.readlines()
    count2 = 0
    count3 = 0
    for l in lines:
        added2 = False
        added3 = False
        results = collections.Counter(l)
        for L in l:
            if results[L] == 2 and not added2:
                count2+=1
                added2 = True
            elif results[L] == 3 and not added3:
                count3+=1
                added3 = True
    print(count2 * count3)
