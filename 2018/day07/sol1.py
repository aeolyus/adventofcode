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
tree = createTree(edges)
done = []
while len(verts) > 0:
    todo = next_todo(tree)
    done.append(todo)
    verts.remove(todo)
    if todo in tree.keys():
        tree.pop(todo)
print(''.join(done))
