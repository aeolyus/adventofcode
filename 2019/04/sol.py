count = 0
for num in range(108457, 562041 + 1):
    dec = True
    adj = True

    temp = []
    for i in str(num):
        i = int(i)
        if temp:
            # Nondecreasing
            if temp[len(temp) - 1] <= i:
                # Adjacent digits are same
                if temp[len(temp) - 1] == i:
                    adj = False
                temp.append(i)
            else:
                dec = False
        else:
            temp = [i]

    if not adj and dec:
        count += 1
print(count)

count = 0
for num in range(108457, 562041 + 1):
    dec = True
    adj = 0
    ok = False

    temp = []
    for i in str(num):
        i = int(i)
        if temp:
            # Nondecreasing
            if temp[len(temp) - 1] <= i:
                # Adjacent digits are same
                if temp[len(temp) - 1] == i:
                    adj += 1
                else:
                    if adj == 1:
                        ok = True
                    adj = 0
                temp.append(i)
            else:
                dec = False
        else:
            temp = [i]

    if adj == 1:
        ok = True

    if ok and dec:
        count += 1
print(count)

