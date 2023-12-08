def part1(input_file: str):
    map = {}
    with open(input_file) as f:
        lines = f.readlines()
        instr = lines[0].strip()
        for line in lines[2:]:
            temp = line.split("=")
            key = temp[0].strip()
            rest = temp[1].strip()[1:-1]
            temp_rest = rest.split(",")
            left = temp_rest[0].strip()
            right = temp_rest[1].strip()
            map[key] = (left, right)
        curr = "AAA"
        loops = 0
        while curr != 'ZZZ':
            for char in instr:
                if char == 'L':
                    curr = map[curr][0]
                else:
                    curr = map[curr][1]
            loops += 1
        return loops * len(instr)


if __name__ == '__main__':
    print(part1("input.txt"))
