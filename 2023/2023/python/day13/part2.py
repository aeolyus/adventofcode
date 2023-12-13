def part2(input_file: str):
    patterns = []
    with open(input_file) as f:
        lines = f.readlines()
        pattern = []
        for line in lines:
            line = line.strip()
            if line == "":
                patterns.append(pattern)
                pattern = []
            else:
                pattern.append([c for c in line])
        patterns.append(pattern)

    sum = 0
    for pattern in patterns:
        pattern_t = list(zip(*pattern))
        vert = find_reflection(pattern)
        horz = find_reflection(pattern_t)
        sum += vert + horz * 100

    return sum


def find_reflection(pattern):
    left_idxs = [i for i in range(0, len(pattern[0]))]
    right_idxs = [i for i in range(0, len(pattern[0]))]
    found_off_by_one_left = [0 for i in range(len(pattern[0]))]
    found_off_by_one_right = [0 for i in range(len(pattern[0]))]
    for line in pattern:
        ln = line[:]
        for i in left_idxs:
            found_off_by_one_left[i] += is_palindrome_off_by_one(ln[i:])

        ln = line[:]
        for i in right_idxs:
            found_off_by_one_right[i] += is_palindrome_off_by_one(ln[:-i])
    left = float('inf')
    right = float('inf')
    if 1 in found_off_by_one_left:
        left = found_off_by_one_left.index(1)
    elif 1 in found_off_by_one_right:
        right = found_off_by_one_right.index(1)

    ans = 0
    if left < right:
        ans = left + len(pattern[0][left:])/2
    elif right < left:
        ans = len(pattern[0][:-right])/2
    return int(ans)


def is_palindrome(s):
    return len(s) > 0 and len(s) % 2 == 0 and s == s[::-1]


def is_palindrome_off_by_one(s):
    if not (len(s) > 0 and len(s) % 2 == 0):
        return float('inf')
    count = 0
    for i in range(len(s)//2):
        if s[i] != s[-i - 1]:
            count += 1
    return count


if __name__ == '__main__':
    print(part2("input.txt"))
