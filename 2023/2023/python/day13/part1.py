def part1(input_file: str):
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
    for line in pattern:
        ln = line[:]
        new_left_idxs = []
        for i in left_idxs:
            if is_palindrome(ln[i:]):
                new_left_idxs.append(i)
        left_idxs = new_left_idxs

        ln = line[:]
        new_right_idxs = []
        for i in right_idxs:
            if is_palindrome(ln[:-i]):
                new_right_idxs.append(i)
        right_idxs = new_right_idxs
    left = left_idxs[0] if len(left_idxs) > 0 else float('inf')
    right = right_idxs[0] if len(right_idxs) > 0 else float('inf')
    ans = 0
    if left < right:
        ans = left + len(pattern[0][left:])/2
    elif right < left:
        ans = len(pattern[0][:-right])/2
    return int(ans)


def is_palindrome(s):
    return len(s) > 0 and len(s) % 2 == 0 and s == s[::-1]


if __name__ == '__main__':
    print(part1("input.txt"))
