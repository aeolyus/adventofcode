import heapq
from enum import Enum
from collections import defaultdict
from typing import NamedTuple

PARENT = "parent"
F = "f"
G = "g"


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


class Position(NamedTuple):
    row: int
    col: int
    dir: Direction
    straight_count: int

    def coord(self):
        return (self.row, self.col)

    def __str__(self):
        return " ".join(str(s) for s in
                        [self.row, self.col, self.dir, self.straight_count])

    def __repr__(self):
        return " ".join(str(s) for s in
                        [self.row, self.col, self.dir, self.straight_count])

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.row == other.row and self.col == other.col


def part2(input_file: str):
    grid = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            temp = [int(c) for c in line]
            grid.append(temp)

    start = Position(0, 0, Direction.E, 0)
    dest = Position(len(grid) - 1, len(grid[0]) - 1, Direction.E, 0)
    return astar(grid, start, dest)


def astar(grid, start: Position, dest: Position):
    # estimated, heat_loss, position
    pq = [(0, 0, start)]
    heatmap = defaultdict(lambda: float('inf'))
    while pq:
        f, heat_loss, pos = heapq.heappop(pq)
        if pos == dest and pos.straight_count >= 4:
            return heat_loss
        for child in ultra_next_steps(grid, pos):
            new_heat_loss = heat_loss + grid[child.row][child.col]
            if new_heat_loss < heatmap[child]:
                heatmap[child] = new_heat_loss
                h = manhattan_dist(child, dest)
                f = new_heat_loss + h
                heapq.heappush(pq, (f, new_heat_loss, child))


def ultra_next_steps(grid, pos):
    result = []

    curr_dir = pos.dir
    exclude_dir = [curr_dir.right().right()]
    if pos.straight_count >= 10:
        exclude_dir.append(pos.dir)
    if 1 <= pos.straight_count < 4:
        directions = [pos.dir]
    else:
        directions = Direction
    for new_dir in directions:
        row = pos.row
        col = pos.col
        straight_count = 1

        if new_dir in exclude_dir:
            continue

        if new_dir == curr_dir:
            straight_count += pos.straight_count

        if new_dir == Direction.N:
            row -= 1
        elif new_dir == Direction.S:
            row += 1
        elif new_dir == Direction.E:
            col += 1
        elif new_dir == Direction.W:
            col -= 1
        new_pos = Position(
            row,
            col,
            new_dir,
            straight_count,
        )
        if is_valid(grid, new_pos):
            result.append(new_pos)

    return result


def manhattan_dist(pos_a: Position, pos_b: Position):
    return abs(pos_a.row - pos_b.row) \
        + abs(pos_a.col - pos_b.col)


def is_valid(grid, pos):
    return 0 <= pos.row < len(grid) \
        and 0 <= pos.col < (len(grid[0]))


if __name__ == '__main__':
    print(part2("input.txt"))
