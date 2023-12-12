import functools

UNKNOWN = '?'
OPERATIONAL = '.'
DAMAGED = '#'


def part2(input_file: str):
    sum = 0
    spring_conditions = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            temp = line.strip().split(" ")
            springs = temp[0]
            data = temp[1]
            spring_conditions.append(
                [
                    ([*([c for c in springs] + [UNKNOWN])]*5)[:-1]
                    + [OPERATIONAL],
                    [int(i) for i in data.split(",")]*5,
                ]
            )
    for i, item in enumerate(spring_conditions):
        spring, data = item
        spring = tuple(spring)
        data = tuple(data)
        num = arrangements(tuple(spring), tuple(data))
        sum += num
    return sum


@functools.cache
def arrangements(spring: tuple[str], data: tuple[int]):
    spring = list(spring)
    data = list(data)
    if len(data) == 0 and len(spring) == 0:
        return 1
    elif len(data) > 0 and len(spring) == 0:
        return 0
    elif len(data) == 0:
        if spring.count(DAMAGED) == 0:
            return 1
        else:
            return 0

    curr_char = spring[0]
    curr_count = data[0]

    if curr_char == DAMAGED:
        enough_space = len(spring) >= curr_count + 1 \
            and all(c in [DAMAGED, UNKNOWN] for c in spring[:curr_count]) \
            and spring[curr_count] in [OPERATIONAL, UNKNOWN]
        if enough_space:
            spring = tuple(spring[curr_count + 1:])
            data = tuple(data[1:])
            return arrangements(spring, data)
        else:
            return 0
    elif curr_char == UNKNOWN:
        enough_space = len(spring) >= curr_count + 1 \
            and all(c in [DAMAGED, UNKNOWN] for c in spring[:curr_count]) \
            and spring[curr_count] in [OPERATIONAL, UNKNOWN]
        temp = arrangements(tuple(spring[1:]), tuple(data))
        if enough_space:
            spring = tuple(spring[curr_count + 1:])
            data = tuple(data[1:])
            return temp + arrangements(spring, data)
        else:
            return temp
    else:
        spring = tuple(spring[1:])
        data = tuple(data)
        return arrangements(spring, data)


if __name__ == '__main__':
    print(part2("input.txt"))
