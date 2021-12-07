def solve(data, log):
    ps = [int(v) for v in data.split(",")]

    def find(cost):
        i = sum(ps) // len(ps)
        c = sum(cost(abs(i - p)) for p in ps)
        cn = sum(cost(abs(i + 1 - p)) for p in ps)
        di = -1 if c < cn else 1
        if di < 0:
            c, cn = cn, c
        while cn < c:
            i += di
            c, cn = cn, sum(cost(abs(i - p)) for p in ps)
        return c

    yield find(lambda v: v)
    yield find(lambda v: v * (v + 1) // 2)
