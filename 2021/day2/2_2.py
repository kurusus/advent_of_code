with open("data/input.txt") as f:
    input =  map(lambda x: tuple(x.split()), f)
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


