def part1(input_file: str):
    with open(input_file) as f:
        lines = f.readlines()
        for li in lines:
            line = li.strip()
        line = line.split(",")
    v = 0
    for word in line:
        v += hash(word)
    return v


def hash(string):
    curr_value = 0
    for c in string:
        curr_value += ord(c)
        curr_value *= 17
        curr_value %= 256
    return curr_value


if __name__ == '__main__':
    print(part1("input.txt"))
