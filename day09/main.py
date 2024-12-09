with open('input') as f:
    input = f.read().strip()

blocks = []
iter = 0
for i in range(len(input)):
    blocks += [iter if i % 2 == 0 else '.' for j in range(int(input[i]))]
    if i % 2 == 0:
        iter += 1

j = len(blocks) - 1
i = 0
while True:
    while blocks[i] != '.' and i < len(blocks) - 1:
        i += 1

    while blocks[j] == '.' and j > 0:
        j -= 1

    if i >= j:
        break

    blocks[i], blocks[j] = blocks[j], blocks[i]


part1 = 0
for i in range(len(blocks)):
    if blocks[i] == '.':
        break
    part1 += i * blocks[i]

print(part1)
