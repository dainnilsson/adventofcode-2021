def solve(data, log):
    xs, ys = [0] * 7, [0] * 2
    for v in data.split(","):
        xs[int(v)] += 1
    for f, t in ((0, 80), (80, 256)):
        for t in range(f, t):
            ys[t % 2], xs[t % 7] = xs[t % 7], xs[t % 7] + ys[t % 2]
        yield sum(xs + ys)
