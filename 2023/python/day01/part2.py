
str_num_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def part2(input_file: str):
    sum = 0
    with open(input_file) as f:
        for line in f:
            num = 0
            first_num_str_map_idx = dict()
            second_num_str_map_idx = dict()
            for idx, char in enumerate(line):
                if ord(char) >= 49 and ord(char) <= 57:
                    first_num_str_map_idx[int(char)] = min(
                        first_num_str_map_idx.get(int(char), float('inf')),
                        idx)
            for idx, char in enumerate(line[::-1]):
                if ord(char) >= 49 and ord(char) <= 57:
                    second_num_str_map_idx[int(char)] = max(
                        second_num_str_map_idx.get(int(char), float('-inf')),
                        len(line) - idx - 1)
            for word in str_num_map:
                i = line.find(word)
                if i >= 0:
                    first_num_str_map_idx[str_num_map[word]] = min(
                        first_num_str_map_idx.get(
                            str_num_map[word], float('inf')),
                        i)
                i = line.rfind(word)
                if i >= 0:
                    second_num_str_map_idx[str_num_map[word]] = max(
                        second_num_str_map_idx.get(
                            str_num_map[word], float('-inf')),
                        i)
            num += min(first_num_str_map_idx.items(),
                       key=lambda x: x[1])[0] * 10
            num += max(second_num_str_map_idx.items(), key=lambda x: x[1])[0]
            sum += num
    return sum


if __name__ == '__main__':
    print(part2("input.txt"))
