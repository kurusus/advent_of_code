with open("data/input.txt") as f:
    input =  map(lambda x: tuple(x.split()), f)
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

