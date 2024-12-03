import re

with open('input') as f:
    input = f.read().strip()

result1 = 0
result2 = 0
enabled = True
for i in range(len(input) - 4):
    if input[i:i + 4] == "do()":
        enabled = True
    if input[i:min(i+7, len(input))] == "don't()":
        enabled = False
    if input[i:i+4] == "mul(":
        end = re.search("\)", input[i+4:])
        numbers = input[i+4:i+4+end.start()].split(",")
        if len(numbers) == 2 and numbers[0].isdigit() and numbers[1].isdigit():
            result1 += int(numbers[0])*int(numbers[1])
            if enabled:
                result2 += int(numbers[0]) * int(numbers[1])

print(result1)
print(result2)
