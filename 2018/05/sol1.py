line = open("input").read().splitlines()[0]
old = "old"
while old != line:
    old = line
    for i in range(0,26):
        line = line.replace(chr(ord("a") + i) + chr(ord("A") + i),"")
        line = line.replace(chr(ord("A") + i) + chr(ord("a") + i),"")
print(len(line))
