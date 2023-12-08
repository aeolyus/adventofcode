import math


def part2(input_file: str):
    currs = {}
    map = {}
    with open(input_file) as f:
        lines = f.readlines()
        instr = lines[0].strip()
        for line in lines[2:]:
            temp = line.split("=")
            key = temp[0].strip()
            if key[-1] == 'A':
                currs[key] = 0
            rest = temp[1].strip()[1:-1]
            temp_rest = rest.split(",")
            left = temp_rest[0].strip()
            right = temp_rest[1].strip()
            map[key] = (left, right)
        for c in currs.keys():
            count = 0
            curr = c
            while curr[-1] != 'Z':
                for char in instr:
                    if char == 'L':
                        curr = map[curr][0]
                    else:
                        curr = map[curr][1]
                    count += 1
            currs[c] = count
        return math.lcm(*currs.values())


if __name__ == '__main__':
    print(part2("input.txt"))
