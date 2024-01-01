def part1(input_file: str):
    answer = 0
    with open(input_file) as f:
        for line in f:
            tmp = line.split("|")
            winning = tmp[0].split(":")[1:][0]
            your_nums = tmp[1].strip()
            nums = [int(i) for i in your_nums.split(" ") if i != '']
            winning_nums = [int(i) for i in winning.split(" ") if i != '']
            points = 0
            for num in nums:
                if num in winning_nums:
                    if points == 0:
                        points = 1
                    else:
                        points *= 2
            answer += points
        return answer


if __name__ == '__main__':
    print(part1("input.txt"))
