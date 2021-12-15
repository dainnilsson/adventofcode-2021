def solve(data, log):
    lines = data.splitlines()
    template = lines[0]
    rules = {k: v for k, v in [line.split(" -> ") for line in lines[2:]]}
    ps = {k: 0 for k in rules}
    for i in range(1, len(template)):
        ps[template[i - 1] + template[i]] += 1

    for r in (10, 30):
        for _ in range(r):
            psn = {k: 0 for k in rules}
            for (a, b), n in ps.items():
                v = rules[a + b]
                psn[a + v] += n
                psn[v + b] += n
            ps = psn

        counts = {c: 0 for c in set("".join(rules.keys()))}
        counts[template[0]] += 1
        for k, n in ps.items():
            counts[k[1]] += n

        yield max(counts.values()) - min(counts.values())
