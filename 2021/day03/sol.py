def solution1(input_file: str):
    with open(input_file) as f:
        arr = []
        for line in f:
            arr.append(line.strip())

        bit_len = len(arr[0])
        arr_len = len(arr)

        col_bit_sum = {}
        for line in arr:
            for i in range(bit_len):
                col_bit_sum[i] = col_bit_sum.get(i, 0) + int(line[i])

        res = []
        for i in range(bit_len):
            if col_bit_sum[i] > arr_len/2:
                res.append(1)
            else:
                res.append(0)

        binary = ''.join(str(x) for x in res)
        gamma = int(binary, 2)
        epsilon = int(''.join('1' if x == '0' else '0' for x in binary), 2)
        print(f"day03 q1: {gamma * epsilon}")

def solution2(input_file: str):
    with open(input_file) as f:
        arr = []
        for line in f:
            arr.append(line.strip())

        bit_len = len(arr[0])
        col_bit_sum = {}
        arr_len = len(arr)
        for line in arr:
            for i in range(bit_len):
                col_bit_sum[i] = col_bit_sum.get(i, 0) + int(line[i])

        res = []
        oxygen_arr = arr
        for i in range(bit_len):
            new_arr = []
            for num in oxygen_arr:
                if col_bit_sum[i] >= len(oxygen_arr)/2:
                    if num[i] == '1':
                        new_arr.append(num)
                else:
                    if num[i] == '0':
                        new_arr.append(num)
            oxygen_arr = new_arr
            col_bit_sum = {}
            for line in oxygen_arr:
                for i in range(bit_len):
                    col_bit_sum[i] = col_bit_sum.get(i, 0) + int(line[i])
            if len(oxygen_arr) <= 1:
                break

        col_bit_sum = {}
        arr_len = len(arr)
        for line in arr:
            for i in range(bit_len):
                col_bit_sum[i] = col_bit_sum.get(i, 0) + int(line[i])

        res = []
        c02_arr = arr
        for i in range(bit_len):
            new_arr = []
            for num in c02_arr:
                if col_bit_sum[i] >= len(c02_arr)/2:
                    if num[i] == '0':
                        new_arr.append(num)
                else:
                    if num[i] == '1':
                        new_arr.append(num)
            c02_arr = new_arr
            col_bit_sum = {}
            for line in c02_arr:
                for i in range(bit_len):
                    col_bit_sum[i] = col_bit_sum.get(i, 0) + int(line[i])
            if len(c02_arr) <= 1:
                break
    oxygen = int(''.join(str(x) for x in oxygen_arr), 2)
    c02 = int(''.join(str(x) for x in c02_arr), 2)
    print(f"day03 q2: {oxygen * c02}")

try:
    solution1("input")
    solution2("input")
except FileNotFoundError:
    print("No input file!")
