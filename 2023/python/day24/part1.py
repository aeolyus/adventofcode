class Hailstone:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz

        self.a = vy
        self.b = -vx
        self.c = vy*x - vx*y


def part1(input_file: str, boundary=[200000000000000, 400000000000000]):
    hailstones = []
    with open(input_file) as f:
        lines = f.readlines()
        for h, line in enumerate(lines):
            temp = line.strip().split("@")
            pos = [int(i) for i in temp[0].strip().split(",")]
            v = [int(i) for i in temp[1].strip().split(",")]
            hailstones.append(Hailstone(*pos, *v))

    result = 0
    for i, h1 in enumerate(hailstones):
        for h2 in hailstones[:i]:
            if parallel(h1, h2):
                continue
            x, y = intersection(h1, h2)

            if not (boundary[0] <= x <= boundary[1]
                    and boundary[0] <= y <= boundary[1]):
                continue

            # Check if in past
            if not all(
                    ((x-h.x) * h.vx) >= 0
                    and (y - h.y) * h.vy >= 0
                    for h in (h1, h2)
            ):
                continue

            result += 1
    return result


def parallel(h1: Hailstone, h2: Hailstone):
    return h1.b * h2.a == h1.a * h2.b


def intersection(h1: Hailstone, h2: Hailstone):
    x = (h1.c*h2.b - h2.c*h1.b)/(h1.a*h2.b-h2.a*h1.b)
    y = (h1.c*h2.a - h2.c*h1.a)/(h1.b*h2.a-h2.b*h1.a)
    return x, y


if __name__ == "__main__":
    print(part1("input.txt"))
