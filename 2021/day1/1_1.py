with open("data/input.txt") as f:
    input = [int(x) for x in f]


increment_count = 0

for i in range(1, len(input)):
    if input[i] > input[i-1]:
        increment_count += 1

print(increment_count)

