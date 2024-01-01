f = open('input').readlines()
total = 0
for line in f:
    total += int(int(line)/3) - 2
print(total)

total = 0
for line in f:
    temp = int(int(line)/3) - 2
    total += temp
    while temp > 0:
        temp = int(temp/3) - 2
        if temp > 0:
            total += temp
        else:
            break
print(total)
