import math


def quadratic_formula(a, b, c):
    return (
        (-b-math.sqrt(b**2 - 4 * a * c))/(2*a),
        (-b+math.sqrt(b**2 - 4 * a * c))/(2*a),
    )


def get_range(tpl: tuple):
    a = max(tpl)
    b = min(tpl)
    return math.ceil(a) - math.floor(b) - 1


def part2(input_file: str):
    t, d = 0, 0
    with open(input_file) as f:
        for line in f:
            if "Time" in line:
                t = int(line.split(":")[1].strip().replace(" ", ""))
            else:
                d = int(line.split(":")[1].strip().replace(" ", ""))
    return get_range(quadratic_formula(-1, t, -d))


if __name__ == '__main__':
    print(part2("input.txt"))
