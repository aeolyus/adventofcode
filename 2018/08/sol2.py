lines = open("input").read().split()

data = []
def add_Node(index):
    childs = int(lines[index])
    metas = int(lines[index + 1])
    index += 2
    val = {}
    for i in range(childs):
        index, v = add_Node(index)
        val[i + 1] = v
    meta_data = []
    for j in range(metas):
        meta_data.append(int(lines[index + j]))
        data.append(int(lines[index + j]))
    index += metas
    return (index, sum(val.get(k, 0) for k in meta_data)) if childs else (index, sum(meta_data))
a, b = add_Node(0)
print(b)
