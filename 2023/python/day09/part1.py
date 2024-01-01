def part1(input_file: str):
    sum = 0
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            arr = [int(i) for i in line.split(" ")]
            sum += next_num(generate_till_zero(arr))
    return sum


def next_num(lst):
    return sum(map(lambda x: x[-1], lst))


def generate_till_zero(lst):
    result = [lst]
    next = lst[:]
    while not all_zero(next):
        next = [a - b for a, b in zip(next[1:], next[:])]
        result.append(next)
    return result


def all_zero(lst):
    return all(v == 0 for v in lst)


if __name__ == '__main__':
    print(part1("input.txt"))
