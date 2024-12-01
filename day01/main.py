def solve():
    input = [line.strip().split() for line in open('input', 'r')]
    left = sorted([int(n[0]) for n in input])
    right = sorted([int(n[1]) for n in input])

    sum = 0
    for i in range(len(input)):
        sum += abs(left[i] - right[i])

    return sum

def solve2():
    input = [line.strip().split() for line in open('input', 'r')]
    left = [int(n[0]) for n in input]
    right = [int(n[1]) for n in input]

    sum = 0
    for n in left:
        sum += n * right.count(n)

    return sum

print(solve())
print(solve2())
