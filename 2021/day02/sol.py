def solution1(input_file: str):
    with open(input_file) as f:
        arr = []
        forward = 0
        depth = 0
        for line in f:
            if "forward" in line:
                num = line.split(" ")[1]
                forward += int(num)
            elif "down" in line:
                num = line.split(" ")[1]
                depth -= int(num)
            else:
                num = line.split(" ")[1]
                depth += int(num)
        print(f"day01 q1: {forward * depth}")

def solution2(input_file: str):
    with open(input_file) as f:
        arr = []
        forward = 0
        depth = 0
        aim = 0
        for line in f:
            if "forward" in line:
                num = line.split(" ")[1]
                forward += int(num)
                depth -= aim * int(num)
            elif "down" in line:
                num = line.split(" ")[1]
                # depth -= int(num)
                aim += int(num)
            else:
                num = line.split(" ")[1]
                # depth += int(num)
                aim -= int(num)
        print(f"day02 q2: {forward * depth}")

try:
    solution1("input")
    solution2("input")
except FileNotFoundError:
    print("No input file!")
