from enum import Enum
EMPTY = '.'
VER_SPLIT = '|'
HOR_SPLIT = '-'
FORWARD_SLASH_MIRROR = '/'
BACKWARD_SLASH_MIRROR = '\\'


class Direction(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

    def right(self):
        v = (self.value + 1) % len(Direction)
        return Direction(v)

    def left(self):
        v = (self.value - 1) % len(Direction)
        return Direction(v)


class Position:
    row: int
    col: int
    dir: Direction

    def __init__(self, row, col, dir):
        self.row = row
        self.col = col
        self.dir = dir

    def __str__(self):
        return " ".join(str(s) for s in [self.row, self.col, self.dir])

    def __repr__(self):
        return " ".join(str(s) for s in [self.row, self.col, self.dir])


def part1(input_file: str):
    grid = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            temp = [c for c in line]
            grid.append(temp)
    e_grid = energized_grid(grid)
    result = count_energized_tiles(e_grid)
    return result


# Returns grid of places where light passes through
def energized_grid(grid):
    cache = [[set() for _ in range(len(grid[0]))] for _ in range(len(grid))]
    result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    stack = [Position(0, 0, Direction.E)]

    while len(stack) > 0:
        pos = stack.pop()

        if not is_valid(grid, pos) or str(pos) in cache[pos.row][pos.col]:
            continue

        cache[pos.row][pos.col].add(str(pos))
        result[pos.row][pos.col] += 1

        char = grid[pos.row][pos.col]
        if char == EMPTY \
                or (char == VER_SPLIT
                    and pos.dir in [Direction.N, Direction.S]) \
                or (char == HOR_SPLIT
                    and pos.dir in [Direction.E, Direction.W]):
            # Move
            next = Position(pos.row, pos.col, pos.dir)
            if pos.dir == Direction.E:
                next.col += 1
            elif pos.dir == Direction.W:
                next.col -= 1
            elif pos.dir == Direction.N:
                next.row -= 1
            elif pos.dir == Direction.S:
                next.row += 1
            stack.append(next)
        elif char == VER_SPLIT:
            next1 = Position(pos.row - 1, pos.col, Direction.N)
            next2 = Position(pos.row + 1, pos.col, Direction.S)
            stack.append(next1)
            stack.append(next2)
        elif char == HOR_SPLIT:
            next1 = Position(pos.row, pos.col + 1, Direction.E)
            next2 = Position(pos.row, pos.col - 1, Direction.W)
            stack.append(next1)
            stack.append(next2)
        elif char == FORWARD_SLASH_MIRROR:
            next = Position(pos.row, pos.col, pos.dir)
            if next.dir in [Direction.N, Direction.S]:
                if next.dir == Direction.N:
                    next.col += 1
                else:
                    next.col -= 1
                next.dir = next.dir.right()
            else:
                if next.dir == Direction.W:
                    next.row += 1
                else:
                    next.row -= 1
                next.dir = next.dir.left()
            stack.append(next)
        elif char == BACKWARD_SLASH_MIRROR:
            next = Position(pos.row, pos.col, pos.dir)
            if next.dir in [Direction.N, Direction.S]:
                if next.dir == Direction.N:
                    next.col -= 1
                else:
                    next.col += 1
                next.dir = next.dir.left()
            else:
                if next.dir == Direction.W:
                    next.row -= 1
                else:
                    next.row += 1
                next.dir = next.dir.right()
            stack.append(next)

    return result


def count_energized_tiles(grid):
    count = 0
    for line in grid:
        for c in line:
            if c > 0:
                count += 1
    return count


def is_valid(grid, pos):
    return 0 <= pos.row < len(grid) \
        and 0 <= pos.col < (len(grid[0]))


if __name__ == '__main__':
    print(part1("input.txt"))
