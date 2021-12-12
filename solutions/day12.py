def solve(data, log):
    paths = {}
    for line in data.splitlines():
        f, t = line.split("-")
        paths.setdefault(f, []).append(t)
        paths.setdefault(t, []).append(f)

    for extra in (False, True):
        found = 0
        visit = [(["start"], extra)]
        while visit:
            p, e = visit.pop(0)
            for f in paths.get(p[-1], []):
                if f == "end":
                    found += 1
                elif f.isupper() or f not in p:
                    visit.append((p + [f], e))
                elif e and f != "start":
                    visit.append((p + [f], False))
        yield found
