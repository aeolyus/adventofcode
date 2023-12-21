from collections import defaultdict

ROCK = "#"
PLOT = "."
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def part1(input_file: str, steps=64):
    garden = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            garden.append(tuple(c for c in line))
    garden = tuple(garden)
    rows = len(garden)
    cols = len(garden)
    start = (rows//2, cols//2)
    return iter_djikstra(garden, start, steps)


def iter_djikstra(garden, start, max_step_count):
    iter_cache = defaultdict(lambda: 0)
    iter_visited = defaultdict(lambda: 0)
    stack = [(max_step_count, start)]
    while stack:
        item = stack[-1]
        step_count, pos = item
        row, col = pos
        if step_count == 0:
            iter_cache[item] += 1
            stack.pop()
            continue

        neighbors_not_in_cache = 4
        for d in DIRECTIONS:
            new_pos = (row + d[0], col + d[1])
            new_item = (step_count - 1, new_pos)
            if not is_valid(garden, new_pos):
                iter_cache[item] += 0
                neighbors_not_in_cache -= 1
            elif new_item in iter_cache:
                iter_cache[item] += 0
                if new_item not in iter_visited:
                    iter_cache[item] += iter_cache[new_item]
                    iter_visited[new_item] = 0
                else:
                    iter_visited[new_item] += 1
                neighbors_not_in_cache -= 1

            else:
                stack.append(new_item)

        if neighbors_not_in_cache == 0:
            stack.pop()

    return iter_cache[(max_step_count, start)]


def is_valid(garden, pos):
    row, col = pos
    return 0 <= row < len(garden) and 0 <= col < len(garden[0]) \
        and garden[row][col] in [PLOT, "S"]


if __name__ == "__main__":
    print(part1("input.txt"))
