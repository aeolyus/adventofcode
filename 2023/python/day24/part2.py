class Hailstone:
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz


def part2(input_file: str, boundary=[200000000000000, 400000000000000]):
    hailstones = []
    with open(input_file) as f:
        lines = f.readlines()
        for h, line in enumerate(lines):
            temp = line.strip().split("@")
            pos = [int(i) for i in temp[0].strip().split(",")]
            v = [int(i) for i in temp[1].strip().split(",")]
            hailstones.append(Hailstone(*pos, *v))

    result = 0
    A = []
    B = []
    for i in range(4):
        h1 = hailstones[i]
        h2 = hailstones[(i + 1)]
        a = h1.vy - h2.vy
        b = h2.vx - h1.vx
        d = h2.y - h1.y
        e = h1.x - h2.x
        rhs = h2.y*h2.vx - h1.y*h1.vx + h1.x*h1.vy-h2.x*h2.vy
        A.append([a, b, d, e])
        B.append(rhs)
    a, b, d, e = gaussian_elimination(A, B)

    h1 = hailstones[0]
    h2 = hailstones[1]
    t1 = (a - h1.x)/(h1.vx - d)
    t2 = (a - h2.x)/(h2.vx - d)
    c1 = h1.z + t1 * h1.vz
    c2 = h2.z + t2 * h2.vz
    f = (c2 - c1)/(t2 - t1)
    c = c1 - f*t1

    a = round(a)
    b = round(b)
    c = round(c)

    return int(a + b + c)

    return result


def gaussian_elimination(A, b):
    n = len(b)
    # Forward elimination
    # a_ij = a_ij - a_ik/a_kk * a_kj
    # b_i = b_i - a_ik/a_kk * b_k
    # k: diagonals, 0 to n-2
    # i: rows, k+1 to n-1
    # j: cols, k to n-1
    for k in range(n-1):
        for i in range(k + 1, n):
            ratio = A[i][k]/A[k][k]
            for j in range(k, n):
                A[i][j] -= ratio * A[k][j]
            b[i] -= ratio*b[k]

    # Back substitution
    # x_n-1 = b_n-1/A_n-1,n-1
    # x_i = (b_i - sum_j(a_ij * x_j))/a_ii
    # i = n-2 to 0
    # j = i+1 to n-1
    x = [0 for _ in range(n)]

    x[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-2, -1, -1):
        sum_j = 0
        for j in range(i+1, n):
            sum_j += A[i][j]*x[j]
        x[i] = (b[i] - sum_j)/A[i][i]

    return x


if __name__ == "__main__":
    print(part2("input.txt"))
