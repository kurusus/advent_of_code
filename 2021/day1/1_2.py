with open("data/input.txt") as f:
    input = [int(x) for x in f]

increment_count = 0

for i in range(3, len(input)):
    if input[i] > input[i-3]:
        increment_count += 1

print(increment_count)

