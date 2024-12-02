def check_row(arr):
    decreasing = None
    for i in range(len(arr) - 1):
        dif = arr[i + 1] - arr[i]
        decreasing = dif < 0 if decreasing is None else decreasing
        if not 1 <= abs(dif) <= 3 or (decreasing and dif > 0) or (not decreasing and dif < 0):
            return False
    return True


def solve():
    input = [line.strip().split() for line in open('input')]
    reports = [[int(n) for n in line] for line in input]

    sum = 0
    for levels in reports:
        sum += check_row(levels)

    return sum


def solve2():
    input = [line.strip().split() for line in open('input')]
    reports = [[int(n) for n in line] for line in input]

    sum = 0
    for levels in reports:
        sum += True in [check_row(levels[:i] + levels[i+1:]) for i in range(len(levels))]

    return sum


print(solve())
print(solve2())
