with open('input') as f:
    rules, updates = f.read().strip().split('\n\n')
    rules = [list(map(int, line.split('|'))) for line in rules.splitlines()]
    updates = [list(map(int, line.split(','))) for line in updates.splitlines()]

result1 = 0
result2 = 0
for update in updates:
    correct = True
    for i in range(len(update) - 1):
        before = [rule for rule in rules if update[i] == rule[1]]
        for rule in before:
            if rule[0] in update and rule[0] not in update[:i]:
                correct = False

        after = [rule for rule in rules if update[i] == rule[0]]
        for rule in after:
            if rule[1] in update and rule[1] not in update[i + 1:]:
                correct = False

    if correct:
        result1 += update[len(update) // 2]

print(result1)