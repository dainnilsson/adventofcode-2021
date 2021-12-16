def solve(data, log):
    def caves():
        lines = data.splitlines()
        mx = len(lines[0])
        my = len(lines)
        cave = {(x, y): int(lines[y][x]) for y in range(my) for x in range(mx)}
        yield cave, mx, my
        yield {
            (i * mx + x, j * my + y): (v - 1 + i + j) % 9 + 1
            for (x, y), v in cave.items()
            for i in range(5)
            for j in range(5)
        }, mx * 5, my * 5

    for cave, mx, my in caves():
        t = (mx - 1, my - 1)
        explored = set()
        visit = {0: [(0, 0)]}
        while visit:
            c = min(visit.keys())
            for p in visit.pop(c):
                if p not in explored:
                    nc = c + cave[p]
                    if p == t:
                        visit = {}
                        yield nc - cave[(0, 0)]
                        break
                    explored.add(p)
                    x, y = p
                    new = visit.setdefault(nc, [])
                    for dx, dy in ((x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)):
                        if (dx, dy) not in explored and 0 <= dx < mx and 0 <= dy < my:
                            new.append((dx, dy))
