def part2(input_file: str):
    mapping = {}
    instances = {}
    with open(input_file) as f:
        # Preprocess
        for cardNum, line in enumerate(f):
            cardNum += 1
            tmp = line.split("|")
            winning = tmp[0].split(":")[1:][0]
            yourNums = tmp[1].strip()
            nums = [int(i) for i in yourNums.split(" ") if i != '']
            winningNums = [int(i) for i in winning.split(" ") if i != '']
            points = 0
            for num in nums:
                if num in winningNums:
                    points += 1
            mapping[cardNum] = points
            instances[cardNum] = 1

        todo = list(mapping.keys())
        while len(todo) > 0:
            cardNum = todo.pop(0)
            matches = mapping[cardNum]
            for i in range(0, matches):
                instances[cardNum + i + 1] += 1 * instances[cardNum]
    return sum(instances.values())


if __name__ == '__main__':
    print(part2("input.txt"))
