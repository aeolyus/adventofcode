NS = '|'
EW = '-'
NE = 'L'
NW = 'J'
SW = '7'
SE = 'F'
S = 'S'
G = '.'

PIPES = [NS, EW, NE, NW, SW, SE]

NORTH = "N"
SOUTH = "S"
EAST = "E"
WEST = "W"

ALL_DIRS = [NORTH, SOUTH, EAST, WEST]

NORTH_PIPES = [NS, SW, SE]
SOUTH_PIPES = [NS, NW, NE]
EAST_PIPES = [EW, NW, SW]
WEST_PIPES = [EW, NE, SE]

COMPAT_PIPES = {
    NORTH: NORTH_PIPES,
    SOUTH: SOUTH_PIPES,
    EAST: EAST_PIPES,
    WEST: WEST_PIPES,
}

DIRECTIONS = {
    S: ALL_DIRS,
    NS: [NORTH, SOUTH],
    EW: [EAST, WEST],
    NE: [NORTH, EAST],
    NW: [NORTH, WEST],
    SW: [SOUTH, WEST],
    SE: [SOUTH, EAST],
    G: [],
}


def part1(input_file: str):
    graph = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            graph.append([char for char in line.strip()])
    s = find_s(graph)
    start, end = neighbors(graph, s)

    dist_map = {start: 0}
    curr_dist = 0
    curr = start
    stack = [start]
    visited = []
    while curr != end:
        curr = stack.pop()
        curr_dist = dist_map.get(curr, float('inf'))
        visited.append(curr)
        nbs = [n for n in neighbors(graph, curr)]
        for n in nbs:
            dist_map[n] = min(dist_map.get(n, float("inf")), curr_dist + 1)
            if n not in visited:
                stack.append(n)
    # Add two to account for start and end both offset by one
    return (dist_map[end] + 2)/2


def find_s(graph):
    for row, line in enumerate(graph):
        for col, char in enumerate(line):
            if char == S:
                return (row, col)


def neighbors(graph, coord):
    neighbors = []
    row, col = coord
    curr = graph[row][col]
    directions = DIRECTIONS[curr]
    for d in directions:
        next = (-1, -1)
        if d is NORTH:
            next = (row - 1, col)
        elif d is SOUTH:
            next = (row + 1, col)
        elif d is EAST:
            next = (row, col + 1)
        elif d is WEST:
            next = (row, col - 1)
        if valid_next(graph, coord, next):
            neighbors.append(next)
    return neighbors


def get_direction(coord, next):
    row, col = coord
    next_row, next_col = next
    if next_row < row:
        return NORTH
    elif next_row > row:
        return SOUTH
    elif next_col > col:
        return EAST
    elif next_col < col:
        return WEST


def valid_next(graph, coord, next):
    next_row, next_col = next
    row, col = coord
    curr_char = graph[row][col]
    # Make sure in graph
    if next_row < 0 \
            or next_row >= len(graph) \
            or next_col < 0 \
            or next_col >= len(graph[0]):
        return False
    next_char = graph[next_row][next_col]
    # Check valid neighbors map
    d = get_direction(coord, next)
    if next_char in COMPAT_PIPES[d]:
        return True
    return False


if __name__ == '__main__':
    print(part1("input.txt"))
