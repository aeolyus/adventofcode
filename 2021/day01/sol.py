def solution1(input_file: str):
    with open(input_file) as f:
        arr = []
        for line in f:
            arr.append(int(line))
        last = 0
        count = -1
        for i in arr:
            if i > last:
                count += 1
            last = i
        print(f"day 01 q1: {count}")

def solution2(input_file: str):
    with open(input_file) as f:
        arr = []
        for line in f:
            arr.append(int(line))
        last = 0
        count = -1
        for i in range(len(arr) - 2):
            if sum(arr[i:i+3]) > last:
                count += 1
            last = sum(arr[i:i+3])
        print(f"day 01 q2: {count}")

try:
    solution1("input")
    solution2("input")
except FileNotFoundError:
    print("No input file!")
