from copy import deepcopy

SLIP_N = "^"
SLIP_S = "v"
SLIP_E = ">"
SLIP_W = "<"

NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

DIRECTIONS = [NORTH, SOUTH, EAST, WEST]


def part1(input_file: str):
    grid = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            grid.append([c for c in line.strip()])

    start = (0, 1)
    end = (len(grid) - 1, len(grid[0]) - 2)

    return longest_path(grid, start, end)


def longest_path(grid, start, end):
    results = []
    stack = [(start, None, 0)]
    while stack:
        pos, prev, count = stack.pop()
        row, col = pos

        if pos == end:
            results.append(count)

        if grid[row][col] == SLIP_N:
            new_pos = tuple(map(sum, zip(pos, NORTH)))
            if new_pos != prev:
                stack.append((new_pos, pos, count + 1))
        elif grid[row][col] == SLIP_E:
            new_pos = tuple(map(sum, zip(pos, EAST)))
            if new_pos != prev:
                stack.append((new_pos, pos, count + 1))
        elif grid[row][col] == SLIP_S:
            new_pos = tuple(map(sum, zip(pos, SOUTH)))
            if new_pos != prev:
                stack.append((new_pos, pos, count + 1))
        elif grid[row][col] == SLIP_W:
            new_pos = tuple(map(sum, zip(pos, WEST)))
            if new_pos != prev:
                stack.append((new_pos, pos, count + 1))
        else:
            for d in DIRECTIONS:
                new_pos = tuple(map(sum, zip(pos, d)))
                if is_valid(new_pos, grid) and new_pos != prev:
                    stack.append((new_pos, pos, count + 1))
    return max(results)


def is_valid(pos, grid):
    row, col = pos
    return 0 <= row < len(grid) \
        and 0 <= col < len(grid[0]) \
        and grid[row][col] != "#"


if __name__ == "__main__":
    print(part1("input.txt"))
