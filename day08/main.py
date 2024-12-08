with open('input') as f:
    input = f.read().strip().splitlines()

locations = set()
locations2 = set()
for i in range(len(input)):
    for j in range(len(input[i])):
        if input[i][j] == '.':
            continue

        freq = input[i][j]
        for k in range(i, len(input)):
            for l in range(j + 1 if k == i else 0, len(input[k])):
                if input[k][l] == freq:
                    dif_vert = k - i
                    dif_hor = l - j

                    loc = (i + 2 * dif_vert, j + 2 * dif_hor)
                    if 0 <= loc[0] < len(input) and 0 <= loc[1] < len(input[i]):
                        locations.add(loc)

                    loc = (i - dif_vert, j - dif_hor)
                    if 0 <= loc[0] < len(input) and 0 <= loc[1] < len(input[i]):
                        locations.add(loc)

                    x = i
                    y = j
                    while 0 <= x < len(input) and 0 <= y < len(input[x]):
                        x -= dif_vert
                        y -= dif_hor

                    x += dif_vert
                    y += dif_hor

                    while 0 <= x < len(input) and 0 <= y < len(input[x]):
                        loc = (x, y)
                        locations2.add(loc)
                        x += dif_vert
                        y += dif_hor


print(len(locations))
print(len(locations2))
