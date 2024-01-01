import itertools


def part2(input_file: str, expand=1000000):
    sum = 0
    universe = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = [char for char in line.strip()]
            universe.append(line)
    is_empty_row = [True for i in range(0, len(universe))]
    for row, line in enumerate(universe):
        for char in line:
            if char == '#':
                is_empty_row[row] = False
                continue

    is_empty_col = [True for i in range(0, len(universe[0]))]
    for line in universe:
        for col, char in enumerate(line):
            if char == '#':
                is_empty_col[col] = False
                continue
    galaxies = get_galaxy_locations(universe)

    sets = list(itertools.combinations(galaxies, 2))

    for pair in sets:
        sum += manhattan_dist(pair[0], pair[1],
                              is_empty_row, is_empty_col, expand)

    return sum


def manhattan_dist(a, b, is_empty_row, is_empty_col, expand):
    a_row, a_col = a
    b_row, b_col = b
    i = min(a_row, b_row)
    j = max(a_row, b_row)
    k = min(a_col, b_col)
    l = max(a_col, b_col)
    result = sum(abs(v1 - v2) for v1, v2 in zip(a, b))
    expanded_rows = is_empty_row[i:j].count(True)
    expanded_cols = is_empty_col[k:l].count(True)
    result += -expanded_rows + expanded_rows * expand
    result += -expanded_cols + expanded_cols * expand
    return result


def get_galaxy_locations(universe):
    result = []
    for row, line in enumerate(universe):
        for col, char in enumerate(line):
            if char == '#':
                result.append((row, col))
    return result


if __name__ == '__main__':
    print(part2("input.txt"))
