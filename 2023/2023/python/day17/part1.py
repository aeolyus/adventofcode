import heapq
from enum import Enum
from collections import defaultdict
from typing import NamedTuple


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

    def __str__(self):
        return " ".join(str(s) for s in
                        [self.row, self.col, self.dir, self.straight_count])

    def __repr__(self):
        return " ".join(str(s) for s in
                        [self.row, self.col, self.dir, self.straight_count])

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.row == other.row and self.col == other.col


def part1(input_file: str):
    grid = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            temp = [int(c) for c in line]
            grid.append(temp)

    start = Position(0, 0, Direction.E, 0)
    dest = Position(len(grid) - 1, len(grid[0]) - 1, Direction.E, 0)
    return dijkstra(grid, start, dest)


# TODO: Optimize with astar
def dijkstra(grid, start: Position, dest: Position):
    # heat_loss, position, path
    pq = [(0, start, [])]
    heatmap = defaultdict(lambda: float('inf'))
    while pq:
        heat_loss, pos, path = heapq.heappop(pq)
        if pos == dest:
            return heat_loss
        for child in next_steps(grid, pos):
            new_heat_loss = heat_loss + grid[child.row][child.col]
            if new_heat_loss < heatmap[child]:
                new_path = path + [child]
                heatmap[child] = new_heat_loss
                heapq.heappush(pq, (new_heat_loss, child, new_path))


def next_steps(grid, pos):
    result = []

    curr_dir = pos.dir
    exclude_dir = curr_dir.right().right()
    for new_dir in Direction:
        row = pos.row
        col = pos.col
        straight_count = 1

        if new_dir == exclude_dir:
            continue

        if new_dir == curr_dir:
            if pos.straight_count >= 3:
                continue
            else:
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


def is_valid(grid, pos):
    return 0 <= pos.row < len(grid) \
        and 0 <= pos.col < (len(grid[0]))


if __name__ == '__main__':
    print(part1("input.txt"))
