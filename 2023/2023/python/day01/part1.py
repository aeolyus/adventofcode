def part1(input_file: str):
    sum = 0
    with open(input_file) as f:
        for line in f:
            num_str = ""
            for char in line:
                if char.isdigit():
                    num_str += char
                    break
            for char in line[::-1]:
                if char.isdigit():
                    num_str += char
                    break
            num = int(num_str)
            sum += num
    return sum


if __name__ == '__main__':
    print(part1("input.txt"))
