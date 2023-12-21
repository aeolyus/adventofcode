from collections import defaultdict

ROCK = "#"
PLOT = "."
DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def part2(input_file: str, step_count=26501365):
    garden = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            garden.append(tuple(c for c in line))
    garden = tuple(garden)
    rows = len(garden)
    cols = len(garden)
    start_row = rows//2
    start_col = cols//2
    start = (rows//2, cols//2)
    garden_len = len(garden)

    odd_full = iter_djikstra(garden, start, len(garden) * 2 + 1)
    even_full = iter_djikstra(garden, start, len(garden) * 2)

    len_full = max(0, step_count//garden_len - 1)

    odds = (((len_full-1)//2) * 2 + 1)**2
    evens = (((len_full + 1)//2) * 2)**2

    steps_to_corner = garden_len//2 + len_full*garden_len + 1
    steps_left_at_corner = step_count - steps_to_corner

    steps_to_big_corner = steps_to_corner - garden_len + garden_len//2 + 1
    steps_left_at_big_corner = step_count - steps_to_big_corner

    # TODO
    steps_to_smol_corner = steps_to_big_corner + garden_len
    steps_left_at_smol_corner = step_count - steps_to_smol_corner

    top_area = iter_djikstra(garden, (0, start_col),
                             steps_left_at_corner)
    bottom_area = iter_djikstra(garden, (garden_len - 1, start_col),
                                steps_left_at_corner)
    left_area = iter_djikstra(garden, (start_row, garden_len - 1),
                              steps_left_at_corner)
    right_area = iter_djikstra(garden, (start_row, 0),
                               steps_left_at_corner)

    num_smol_corner = len_full + 1
    num_big_corner = len_full

    smol_corner_area = iter_djikstra(garden, (0, 0),
                                     steps_left_at_smol_corner)
    ne_smol_corner_area = iter_djikstra(garden, (garden_len - 1, 0),
                                        steps_left_at_smol_corner)
    se_smol_corner_area = iter_djikstra(garden, (0, 0),
                                        steps_left_at_smol_corner)
    nw_smol_corner_area = iter_djikstra(garden,
                                        (garden_len - 1, garden_len - 1),
                                        steps_left_at_smol_corner)
    sw_smol_corner_area = iter_djikstra(garden, (0, garden_len - 1),
                                        steps_left_at_smol_corner)
    big_corner_area = iter_djikstra(garden, (0, 0),
                                    steps_left_at_big_corner)
    ne_big_corner_area = iter_djikstra(garden, (garden_len - 1, 0),
                                       steps_left_at_big_corner)
    se_big_corner_area = iter_djikstra(garden, (0, 0),
                                       steps_left_at_big_corner)
    nw_big_corner_area = iter_djikstra(garden,
                                       (garden_len - 1, garden_len - 1),
                                       steps_left_at_big_corner)
    sw_big_corner_area = iter_djikstra(garden, (0, garden_len - 1),
                                       steps_left_at_big_corner)

    result = odds * odd_full \
        + even_full * evens \
        + top_area + bottom_area + left_area + right_area \
        + num_smol_corner * ne_smol_corner_area \
        + num_smol_corner * nw_smol_corner_area \
        + num_smol_corner * se_smol_corner_area \
        + num_smol_corner * sw_smol_corner_area \
        + num_big_corner * ne_big_corner_area \
        + num_big_corner * nw_big_corner_area \
        + num_big_corner * se_big_corner_area \
        + num_big_corner * sw_big_corner_area
    return result


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
    print(part2("custom-sample.txt"))
