line = open("input").read().splitlines()[0]
smol = len(line)
og = line
for j in range(0, 26):
    line = og
    line = line.replace(chr(ord("a") + j),"")
    line = line.replace(chr(ord("A") + j),"")
    old = "old"
    while old != line:
        old = line
        for i in range(0,26):
            line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
            line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")
    smol = len(line) if smol > len(line) else smol
print(smol)
