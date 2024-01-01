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
    return dfs(dist, start, end)[0]


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
    seen = set()

    def rec_dfs(pos):
        if pos == end:
            return 0, True
        m = 0
        found = False
        seen.add(pos)
        for n in dist[pos]:
            if n not in seen:
                n_count, n_found = rec_dfs(n)
                found |= n_found
                n_count += dist[pos][n]
                if n_found:
                    m = max(m, n_count)
        seen.remove(pos)
        return m, found

    return rec_dfs(start)


def is_valid(pos, grid):
    row, col = pos
    return 0 <= row < len(grid) \
        and 0 <= col < len(grid[0]) \
        and grid[row][col] != "#"


if __name__ == "__main__":
    print(part2("input.txt"))
