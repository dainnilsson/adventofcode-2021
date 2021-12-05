def solve(data, log):
    hv, d = {}, {}
    for line in data.splitlines():
        (x, y), (x2, y2) = [[int(v) for v in f.split(",")] for f in line.split(" -> ")]
        dest = hv if x == x2 or y == y2 else d
        while x != x2 or y != y2:
            dest[(x, y)] = dest.get((x, y), 0) + 1
            x += 1 if x2 > x else -1 if x > x2 else 0
            y += 1 if y2 > y else -1 if y > y2 else 0
        dest[(x, y)] = dest.get((x, y), 0) + 1
    yield sum(1 for v in hv.values() if v > 1)
    yield sum(1 for k in set(hv).union(d) if hv.get(k, 0) + d.get(k, 0) > 1)
