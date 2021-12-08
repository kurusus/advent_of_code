import aocd

input =  map(lambda x: tuple(x.split()), aocd.get_input(2021, 2))
depth = 0
distance = 0
aim = 0
for c, n in input:
    n = int(n)
    if c == "down":
       aim += n
    if c == "up":
       aim -= n
    if c == "forward":
       distance += n
       depth += n*aim
print(depth*distance)

