def part2(input_file: str):
    dig_plan = []
    b = 0
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            temp = line.split(" ")
            color = temp[2][2:-1]
            num = int(color[:5], 16)
            b += num
            direction = color[-1]
            dig_plan.append((direction, num, color))
        coords = get_coords(dig_plan)
        area = shoelace(coords)
        int_area = picks_theorem(area, b)
    return int_area + b


def get_coords(dig_plan):
    start = [0, 0]
    result = [start]
    curr = start[:]
    for line in dig_plan:
        direction, num, color = line
        if direction == '3':
            curr[1] += num
        elif direction == '1':
            curr[1] -= num
        elif direction == '0':
            curr[0] += num
        elif direction == '2':
            curr[0] -= num
        new_point = curr[:]
        if new_point != start:
            result.append(new_point)
    return result


def shoelace(coords):
    sum1 = 0
    sum2 = 0
    for i in range(len(coords) - 1):
        sum1 += coords[i][0] * coords[i + 1][1]
        sum2 += coords[i][1] * coords[i + 1][0]
    sum1 += coords[len(coords) - 1][0] * coords[0][1]
    sum2 += coords[0][0] * coords[len(coords) - 1][1]
    return abs(sum1 - sum2)/2


def picks_theorem(area, b):
    return area - b/2 + 1


if __name__ == '__main__':
    print(part2("input.txt"))
