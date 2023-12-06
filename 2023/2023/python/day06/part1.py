import math
from functools import reduce


def quadratic_formula(a, b, c):
    return (
        (-b-math.sqrt(b**2 - 4 * a * c))/(2*a),
        (-b+math.sqrt(b**2 - 4 * a * c))/(2*a),
    )


def get_range(tpl: tuple):
    a = max(tpl)
    b = min(tpl)
    return math.ceil(a) - math.floor(b) - 1


def part1(input_file: str):
    times = []
    dist = []
    with open(input_file) as f:
        for line in f:
            if "Time" in line:
                temp = line.split(":")[1].strip().split(" ")
                times = [int(i) for i in temp if i != '']
            else:
                temp = line.split(":")[1].strip().split(" ")
                dist = [int(i) for i in temp if i != '']
    best_time_dist = list(zip(times, dist))
    m = map(
        lambda p: get_range(quadratic_formula(-1, p[0], -p[1])),
        best_time_dist,
    )
    return reduce(lambda x, y: x * y, m, 1)


if __name__ == '__main__':
    print(part1("input.txt"))
