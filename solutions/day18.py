def solve(data, log):
    lines = [eval(x) for x in data.splitlines()]

    def add(val, x, left=True):
        if isinstance(val, int):
            return val + x
        lh, rh = val
        return [add(lh, x), rh] if left else [lh, add(rh, x, False)]

    def explode(val, level=0):
        if isinstance(val, int):
            return val, False, 0, 0
        lh, rh = val
        if level < 4:
            lh, c, el, er = explode(lh, level + 1)
            if c:
                return [lh, add(rh, er)], True, el, 0
            rh, c, el, er = explode(rh, level + 1)
            if c:
                return [add(lh, el, False), rh], True, 0, er
            return val, False, 0, 0
        else:
            return 0, True, lh, rh

    def split(val):
        if isinstance(val, int):
            if val > 9:
                x = val // 2
                return [x, val - x], True
            return val, False
        lh, rh = val
        lh, c = split(lh)
        if c:
            return [lh, rh], True
        rh, c = split(rh)
        if c:
            return [lh, rh], True
        return val, False

    def mag(val):
        return val if isinstance(val, int) else 3 * mag(val[0]) + 2 * mag(val[1])

    def red(val):
        while True:
            val, c, _, _ = explode(val)
            if c:
                continue
            val, c = split(val)
            if c:
                continue
            return val

    s = lines[0]
    for x in lines[1:]:
        s = red([s, x])
    yield mag(s)

    yield max(
        mag(red([lines[i], lines[j]]))
        for i in range(len(lines))
        for j in range(len(lines))
        if i != j
    )
