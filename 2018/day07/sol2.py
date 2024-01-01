import re
lines = open("input").read().splitlines()

def createTree(edges_lst):
    tree = {}
    for v1, v2 in edges_lst:
        tree.setdefault(v1, []).append(v2)
    return tree

def next_todo(t):
    for v in verts:
        unique = True
        for values in t.values():
            if v in values:
                unique = False
        if unique:
            return v

verts = set()
edges = []
for line in lines:
    caps = re.findall(r'[A-Z]+', line)
    edges.append([caps[1], caps[2]])
    verts.add(caps[1])
    verts.add(caps[2])

verts = sorted(verts)
verts2 = verts.copy()
tree = createTree(edges)
tree2 = tree.copy()
done = []
while len(verts) > 0:
    todo = next_todo(tree)
    done.append(todo)
    verts.remove(todo)
    if todo in tree.keys():
        tree.pop(todo)

empty = 0
time = 0
workers = {k: None for k in range(5)}
finished = False
while verts2 or any(workers.values()):
    for w in workers:
        if workers[w]:
            ltr, c = workers[w]
            if c == ord(ltr) - ord('A') + 61:
                verts2.remove(ltr)
                if ltr in tree2.keys():
                    tree2.pop(ltr)
                workers[w] = None
            else:
                workers[w] = (ltr, c + 1)
    for w in workers:
        if not workers[w]:
            for x in done:
                uniq = True
                for values in tree2.values():
                    if x in values:
                        uniq = False
                if uniq:
                    workers[w] = (x, 1)
                    done.remove(x)
                    break
    time += 1
print(time - 1)


