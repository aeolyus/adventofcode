def part2(input_file: str):
    platform = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            platform.append([c for c in line.strip()])
    cache = {}
    cycle = 0
    cycles = 1000000000
    cachified_platform = tuple()
    for i in range(cycles):
        for j in range(4):
            platform = tilt_north(platform)
            platform = rotate_right_clockwise(platform)
        cachified_platform = cachify(platform)
        if cachified_platform in cache and cycle <= 0:
            cycle = i - cache[cachified_platform]
        else:
            cache[cachified_platform] = i
        if cycle > 0 and (cycles - i - 1) % cycle == 0:
            break
    return score(platform)


def cachify(platform):
    new_platform = []
    for line in platform:
        new_platform.append(tuple(line))
    return tuple(new_platform)


def score(new_platform):
    sum = 0
    new_platform_t = zip(*new_platform)
    for line in new_platform_t:
        for i, c in enumerate(line):
            multiplier = len(line) - i
            if c == 'O':
                sum += multiplier
    return sum


def rotate_right_clockwise(platform):
    new_platform = []
    for i in range(len(platform)):
        new_line = []
        for line in platform[::-1]:
            new_line.append(line[i])
        new_platform.append(new_line)
    return new_platform


def tilt_north(platform):
    platform_t = list(zip(*platform))
    new_platform_t = []
    for line in platform_t:
        new_line = ['.' for i in range(len(line))]
        left = 0
        for i, c in enumerate(line):
            if c == '.':
                continue
            elif c == "O":
                new_line[left] = c
                left += 1
            elif c == "#":
                new_line[i] = c
                left = i + 1
        new_platform_t.append(new_line)
    new_platform = list(zip(*new_platform_t))
    return new_platform


if __name__ == '__main__':
    print(part2("input.txt"))
