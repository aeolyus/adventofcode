from copy import deepcopy
import random


class UnionFind:

    def __init__(self, lst):
        self.parent = {i: i for i in lst}
        self.sets = len(self.parent)

    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, x, y):
        xrep = self.find(x)
        yrep = self.find(y)
        self.parent[xrep] = yrep
        self.sets -= 1

    def sets(self):
        return self.sets


def part1(input_file: str):
    edges = set()
    vertices = set()
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            temp = line.strip().split(":")
            parent = temp[0]
            children = temp[1].strip().split(" ")
            vertices.add(parent)
            for c in children:
                vertices.add(c)
                if (c, parent) not in edges:
                    edges.add((parent, c))

    uf = condense(vertices, edges)
    groups = list(set(uf.parent.values()))

    a = uf.find(groups[0])
    num_a = 0
    num_b = 0
    for i in uf.parent.values():
        if uf.find(i) == a:
            num_a += 1
        else:
            num_b += 1
    return num_a * num_b


def condense(orig_vertices, orig_edges):
    while True:
        edges = deepcopy(orig_edges)
        uf = UnionFind(orig_vertices)
        while uf.sets > 2:
            x, y = random.choice(list(edges))
            edges.remove((x, y))
            if uf.find(x) == uf.find(y):
                continue
            else:
                uf.union(x, y)

        should_break = 0
        for e in edges:
            x, y = e
            if uf.find(x) != uf.find(y):
                should_break += 1
        if should_break == 3:
            break
    uf.parent.values()
    return uf


if __name__ == "__main__":
    print(part1("input.txt"))
