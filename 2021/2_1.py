import aocd

input =  map(lambda x: tuple(x.split()), aocd.get_input(2021, 2))
depth = 0
distance = 0
for c, n in input:
    n = int(n)
    if c == "down":
       depth += n
    if c == "up":
       depth -= n
    if c == "forward":
       distance += n
print(depth*distance)

