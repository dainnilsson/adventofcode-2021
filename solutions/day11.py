def solve(data, log):
    m = {
        (x, y): int(c)
        for y, line in enumerate(data.splitlines())
        for x, c in enumerate(line)
    }

    a, b, t = 0, 0, 0
    while not b or t < 100:
        m, f = tick(m)
        t += 1
        a += f
        if t == 100:
            yield a
        if f == 100:
            b = t
    yield b


def tick(m):
    m = {p: m[p] + 1 for p in m}
    f = 0
    change = True
    while change:
        change = False
        for p in m:
            if m[p] > 9:
                change = True
                f += 1
                m[p] = 0
                x, y = p
                for q in (
                    (i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2)
                ):
                    if m.get(q, 0) > 0:
                        m[q] += 1
    return m, f
