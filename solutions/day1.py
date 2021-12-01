def solve(data, log):
    xs = [int(line) for line in data.splitlines()]
    yield sum(xs[i] < xs[i + 1] for i in range(len(xs) - 1))
    yield sum(sum(xs[i : i + 3]) < sum(xs[i + 1 : i + 4]) for i in range(len(xs) - 3))
