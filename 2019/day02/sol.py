STOP = 99
ADD = 1
MUL = 2

f = open('input').read().split(',')

def output():
    curr = 0
    while table[curr] != STOP:
        if table[curr] == ADD:
            table[table[curr + 3]] = table[table[curr + 2]] + table[table[curr + 1]]
            curr += 4
        elif table[curr] == MUL:
            table[table[curr + 3]] = table[table[curr + 2]] * table[table[curr + 1]]
            curr += 4
        else:
            break
    return table[0]

# Replace position 1 with '12' and position 2 with '2'
table = {i:int(f[i]) for i in range(len(f))}
table[1] = 12
table[2] = 2
print(output())

for i in range(100):
    for j in range(100):
        table = {i:int(f[i]) for i in range(len(f))}
        table[1] = i
        table[2] = j
        result = output()
        if result == 19690720:
            print(100 * i + j)

