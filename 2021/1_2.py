import aocd

input = aocd.get_input(2021, 1)
input = [int(x) for x in input]

increment_count = 0

for i in range(3, len(input)):
    if input[i] > input[i-3]:
        increment_count += 1

print(increment_count)

