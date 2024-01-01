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

LINES = {
    NE: SW,
    SE: NW,
}


def part2(input_file: str):
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
    stack = [[start]]
    visited = []

    loop_path = []
    while len(stack) > 0:
        path = stack.pop(0)
        curr = path[-1]
        curr_dist = dist_map.get(curr, float('inf'))
        visited.append(curr)
        nbs = [n for n in neighbors(graph, curr)]
        for n in nbs:
            new_path = path[:]
            new_path.append(n)
            dist_map[n] = min(dist_map.get(n, float("inf")), curr_dist + 1)
            if n not in visited:
                stack.append(new_path)
            if n == end:
                loop_path = [s, *new_path]

    # Replace S with proper letter for handling loops
    replacement = replace_s(graph, s)
    s_row, s_col = s
    graph[s_row][s_col] = replacement

    sum = 0
    for row, line in enumerate(graph):
        inside_loop = False
        is_line_stack = []
        for col, char in enumerate(line):
            if not inside_loop:
                if (row, col) in loop_path:
                    if char in [EW]:
                        continue
                    elif char in LINES.keys():
                        is_line_stack.append(char)
                    elif char in LINES.values():
                        prev = is_line_stack.pop()
                        if LINES[prev] == char:
                            inside_loop = not inside_loop
                    else:
                        inside_loop = not inside_loop
            else:
                if (row, col) in loop_path:
                    if char in [EW]:
                        continue
                    elif char in LINES.keys():
                        is_line_stack.append(char)
                    elif char in LINES.values():
                        prev = is_line_stack.pop()
                        if LINES[prev] == char:
                            inside_loop = not inside_loop
                    else:
                        inside_loop = not inside_loop
                elif inside_loop:
                    sum += 1
    return sum


def replace_s(graph, coord):
    row, col = coord
    start, end = neighbors(graph, coord)
    next_row, next_col = end
    row, col = start
    if next_col == col:
        return NS
    elif next_row == row:
        return EW
    elif next_row < row:
        if next_col > col:
            return SE
        elif next_col < col:
            return SW
    elif next_row > row:
        if next_col > col:
            return NE
        elif next_col < col:
            return NW


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
    print(part2("input.txt"))
