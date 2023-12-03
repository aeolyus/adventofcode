from typing import List


def symbol_adjacent(data: List[List[str]], row: int, beg: int, end: int):
    row_count = len(data)
    col_count = len(data[0])
    for i in range(row-1, row + 2):
        for j in range(beg - 1, end + 2):
            if 0 <= i < row_count \
                    and 0 <= j < col_count \
                    and not (i == row and (j >= beg and j <= end)):
                if data[i][j] != '.' \
                        and not data[i][j].isdigit() \
                        and data[i][j] != '\n':
                    return True
    return False


def part1(input_file: str):
    answer = 0
    with open(input_file) as f:
        data = [line for line in f.readlines()]
        for row_num, row in enumerate(data):
            curr_num_str = ""
            curr_num = 0
            beg = -1
            for row_idx, char in enumerate(row):
                if char.isdigit():
                    if beg == -1:
                        beg = row_idx
                    curr_num_str += char
                else:
                    if beg != -1:
                        curr_num = int(curr_num_str)
                        include = symbol_adjacent(
                            data, row_num, beg, row_idx - 1)
                        if include:
                            answer += curr_num
                        beg = -1
                        curr_num_str = ""
    return answer


if __name__ == '__main__':
    print(part1("input.txt"))
