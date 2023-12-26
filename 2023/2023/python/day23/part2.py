from copy import deepcopy

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

DIRECTIONS = [NORTH, SOUTH, EAST, WEST]


def part2(input_file: str):
    grid = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            grid.append([c for c in line.strip()])

    start = (0, 1)
    end = (len(grid) - 1, len(grid[0]) - 2)

    nodes = [start, end] + find_nodes(grid)
    dist = node_dist(nodes, grid)
    return dfs(dist, start, end)


def find_nodes(grid):
    nodes = []
    for row, line in enumerate(grid):
        for col, char in enumerate(line):
            n = 0
            if grid[row][col] != ".":
                continue
            for d in DIRECTIONS:
                new_pos = tuple(map(sum, zip((row, col), d)))
                if is_valid(new_pos, grid):
                    n += 1
            if n >= 3:
                nodes.append((row, col))
    return nodes


def node_dist(nodes, grid):
    dist = {n: {} for n in nodes}
    for n in nodes:
        stack = [(n, 0)]
        seen = set()
        while stack:
            pos, count = stack.pop()
            seen.add(pos)
            if n != pos and pos in nodes:
                dist[n][pos] = count
                continue
            for d in DIRECTIONS:
                new_pos = tuple(map(sum, zip(pos, d)))
                if is_valid(new_pos, grid) and new_pos not in seen:
                    stack.append((new_pos, count + 1))
    return dist


def dfs(dist, start, end):
    result = 0
    stack = [(start, set(), 0)]
    while stack:
        pos, seen, count = stack.pop()
        row, col = pos

        seen = deepcopy(seen)
        seen.add(pos)

        if pos == end:
            result = max(result, count)
        else:
            for new_pos in dist[pos]:
                if new_pos not in seen:
                    stack.append((new_pos, seen, count + dist[pos][new_pos]))
    return result


def is_valid(pos, grid):
    row, col = pos
    return 0 <= row < len(grid) \
        and 0 <= col < len(grid[0]) \
        and grid[row][col] != "#"


if __name__ == "__main__":
    print(part2("input.txt"))
