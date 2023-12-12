import functools

UNKNOWN = '?'
OPERATIONAL = '.'
DAMAGED = '#'


def part1(input_file: str):
    sum = 0
    spring_conditions = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            temp = line.strip().split(" ")
            springs = temp[0] + '.'
            data = temp[1]
            spring_conditions.append(
                [
                    [c for c in springs],
                    [int(i) for i in data.split(",")],
                ]
            )
    for spring, data in spring_conditions:
        spring = tuple(spring)
        data = tuple(data)
        num = arrangements(tuple(spring), tuple(data), tuple())
        sum += num
    return sum


@functools.cache
def arrangements(spring: tuple[str], data: tuple[int], answer: tuple[str]):
    spring = list(spring)
    data = list(data)
    answer = list(answer)
    if len(data) == 0 and len(spring) == 0:
        return 1
    elif len(data) > 0 and len(spring) == 0:
        return 0
    elif len(data) == 0:
        if spring.count(DAMAGED) == 0:
            answer.extend(spring)
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
            answer.extend([DAMAGED for i in range(curr_count)] + ['.'])
            answer = tuple(answer)
            return arrangements(spring, data, answer)
        else:
            return 0
    elif curr_char == UNKNOWN:
        enough_space = len(spring) >= curr_count + 1 \
            and all(c in [DAMAGED, UNKNOWN] for c in spring[:curr_count]) \
            and spring[curr_count] in [OPERATIONAL, UNKNOWN]
        temp = arrangements(
            tuple(spring[1:]), tuple(data), tuple(answer + [OPERATIONAL])
        )
        if enough_space:
            spring = tuple(spring[curr_count + 1:])
            data = tuple(data[1:])
            answer.extend([DAMAGED for i in range(curr_count)] + [OPERATIONAL])
            answer = tuple(answer)
            return temp + arrangements(spring, data, answer)
        else:
            return temp
    else:
        answer = tuple(answer + [spring[0]])
        spring = tuple(spring[1:])
        data = tuple(data)
        return arrangements(spring, data, answer)


if __name__ == '__main__':
    print(part1("input.txt"))
