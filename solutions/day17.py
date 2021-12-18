def solve(data, log):
    tx, ty = [
        [int(v) for v in ln.split("..")] for ln in data.split("x=")[1].split(", y=")
    ]

    times = {}
    fall = {}
    for vx in range(tx[1] + 1):
        x = dx = vx
        t = 1
        while x <= tx[1] and dx:
            dx -= 1
            if x >= tx[0]:
                times.setdefault(t, set()).add(vx)
                if dx == 0:
                    fall[vx] = t
            t += 1
            x += dx

    hits = {}
    for vy in range(ty[0], -ty[0]):
        y = dy = vy
        t = 1
        while y >= ty[0]:
            if y <= ty[1]:
                xs = times.get(t, set()) | {x for x, t2 in fall.items() if t2 < t}
                if xs:
                    hits[vy] = hits.get(vy, set()) | xs
            t += 1
            dy -= 1
            y += dy

    vy = max(hits.keys())
    yield vy * (vy + 1) // 2
    yield sum(len(xs) for xs in hits.values())
