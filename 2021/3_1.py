import aocd


input = aocd.get_input(2021, 3)

bit_count = [0 for i in range(len(input[0]))]
for num in input:
    for i in range(len(num)):
        try:
            bit_count[i] += 1 if num[i] == "1" else -1
        except IndexError:
            print("num unexpected length")           
gamma = int("".join(map(lambda x: "1" if x > 0 else "0", bit_count)), 2)
epsilon = int("".join(map(lambda x: "0" if x > 0 else "1", bit_count)), 2)
print(gamma * epsilon)
