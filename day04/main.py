with open('input') as f:
    input = f.read().splitlines()

xmas = 'XMAS'
result1 = 0
result2 = 0
for i in range(len(input)):
    for j in range(len(input[i])):
        # Horizontal
        if j + 3 < len(input[i]):
            hor = input[i][j] + input[i][j+1] + input[i][j+2] + input[i][j+3]
            result1 += hor == xmas or hor[::-1] == xmas

        # Vertical
        if i + 3 < len(input):
            vert = input[i][j] + input[i+1][j] + input[i+2][j] + input[i+3][j]
            result1 += vert == xmas or vert[::-1] == xmas

            # Diagonal
            if j + 3 < len(input[i]):
                diag = input[i][j] + input[i+1][j+1] + input[i+2][j+2] + input[i+3][j+3]
                result1 += diag == xmas or diag[::-1] == xmas
            if j - 3 >= 0:
                diag2 = input[i][j] + input[i+1][j-1] + input[i+2][j-2] + input[i+3][j-3]
                result1 += diag2 == xmas or diag2[::-1] == xmas

        # Part 2
        if 0 < i < len(input[i]) - 1 and 0 < j < len(input[i]) - 1:
            diag = input[i-1][j-1] + input[i][j] + input[i+1][j+1]
            diag2 = input[i-1][j+1] + input[i][j] + input[i+1][j-1]
            result2 += (diag == xmas[1:] or diag[::-1] == xmas[1:]) and (diag2 == xmas[1:] or diag2[::-1] == xmas[1:])

print(result1)
print(result2)