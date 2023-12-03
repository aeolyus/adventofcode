from typing import List, Dict


def get_adj_nums(
        data: List[List[str]], num_map: Dict[int, int], row: int, col: int
) -> List[int]:
    result_IR = set()
    row_count = len(data)
    col_count = len(data[0])
    for i in range(row-1, row + 2):
        for j in range(col - 1, col + 2):
            if 0 <= i < row_count \
                    and 0 <= j < col_count \
                    and not (i == row and j == col):
                if data[i][j] != '.' and data[i][j] != '\n':
                    k = int(data[i][j])
                    result_IR.add(k)
    return [num_map[i] for i in result_IR]


def create_helper_matrix(data: List[List[str]]) -> List[List[str]]:
    helper_matrix = {}
    return helper_matrix


def part2(input_file: str):
    answer = 0
    with open(input_file) as f:
        data = [line for line in f.readlines()]
        helper_matrix = [['.' for char in line] for line in data]
        num_key = 0
        num_map = {}

        for row_num, row in enumerate(data):
            curr_num_str = ""
            curr_num = 0
            beg = -1
            for row_idx, char in enumerate(row):
                helper_matrix[row_num][row_idx] = char
                if char.isdigit():
                    if beg == -1:
                        beg = row_idx
                    curr_num_str += char
                else:
                    if beg != -1:
                        curr_num = int(curr_num_str)
                        num_map[num_key] = curr_num
                        for i in range(beg, row_idx):
                            helper_matrix[row_num][i] = str(num_key)
                        num_key += 1
                        # Reset
                        beg = -1
                        curr_num_str = ""

        for row_num, row in enumerate(helper_matrix):
            for row_idx, char in enumerate(row):
                if char == '*':
                    nums = get_adj_nums(
                        helper_matrix, num_map, row_num, row_idx)
                    if len(nums) == 2:
                        answer += nums[0] * nums[1]
    return answer


if __name__ == '__main__':
    print(part2("input.txt"))
