lines = open("input").read().split()

data = []
def add_Node(index):
    childs = int(lines[index])
    metas = int(lines[index + 1])
    index += 2
    for i in range(childs):
        index = add_Node(index)
    for j in range(metas):
        data.append(int(lines[index + j]))
    return index + metas
add_Node(0)
print(sum(data))
