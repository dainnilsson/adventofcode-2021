def solve(data, log):
    lines = data.splitlines()
    n = len(lines[0])

    def common(lines):
        arr = [0] * n
        for line in lines:
            for i, v in enumerate(line):
                if v == "1":
                    arr[i] += 1
        return "".join(str(int(c >= len(lines) - c)) for c in arr)

    g = common(lines)
    g_int = int(g, 2)
    yield g_int * (g_int ^ (2 ** n - 1))

    ox = lines
    for i in range(n):
        v = common(ox)[i]
        ox = [x for x in ox if x[i] == v]
        if len(ox) == 1:
            break
    co = lines
    for i in range(n):
        v = common(co)[i]
        co = [x for x in co if x[i] != v]
        if len(co) == 1:
            break
    yield int(ox[0], 2) * int(co[0], 2)
