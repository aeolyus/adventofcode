def part1(input_file: str):
    platform = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            platform.append([c for c in line.strip()])

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
    sum = 0
    for line in new_platform_t:
        for i, c in enumerate(line):
            multiplier = len(line) - i
            if c == 'O':
                sum += multiplier
    return sum


if __name__ == '__main__':
    print(part1("input.txt"))
