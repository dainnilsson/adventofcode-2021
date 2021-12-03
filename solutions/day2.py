def solve(data, log):
    lines = [line.split() for line in data.splitlines()]
    aim, x, y = 0, 0, 0
    for (dr, f) in lines:
        v = int(f)
        if dr == "down":
            aim += v
        elif dr == "up":
            aim -= v
        elif dr == "forward":
            x += v
            y += v * aim

    yield aim * x
    yield x * y
