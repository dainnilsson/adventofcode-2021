def solve(data, log):
    def adj(x, y):
        return (x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)

    m = {}
    for my, line in enumerate(data.splitlines()):
        for mx, c in enumerate(line):
            m[(mx, my)] = int(c)
    ps = [
        (x, y)
        for x in range(mx + 1)
        for y in range(my + 1)
        if all(m.get(p, 9) > m[(x, y)] for p in adj(x, y))
    ]
    yield sum(m[p] + 1 for p in ps)

    def search(p, acc):
        acc.add(p)
        [search(a, acc) for a in adj(*p) if a not in acc and m.get(a, 9) < 9]
        return len(acc)

    a, b, c = list(sorted(search(p, {p}) for p in ps))[-3:]
    yield a * b * c
