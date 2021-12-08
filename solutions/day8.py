def solve(data, log):
    lines = [[frozenset(v) for v in ln.split()] for ln in data.splitlines()]
    yield sum(1 for ln in lines for w in ln[-4:] if len(w) in (2, 4, 3, 7))

    def derive(signal, out):
        def find(c):
            return next(filter(c, signal))

        s = {}
        s[1] = find(lambda w: len(w) == 2)
        s[4] = find(lambda w: len(w) == 4)
        s[7] = find(lambda w: len(w) == 3)
        s[8] = find(lambda w: len(w) == 7)
        s[3] = find(lambda w: len(w) == 5 and w > s[7])
        s[6] = find(lambda w: len(w) == 6 and not w > s[7])
        s[5] = find(lambda w: len(w) == 5 and w < s[6])
        s[2] = find(lambda w: len(w) == 5 and w != s[3] and not w < s[6])
        s[9] = find(lambda w: len(w) == 6 and w != s[6] and w > s[5])
        s[0] = find(lambda w: len(w) == 6 and not w > s[5])
        key = {v: k for k, v in s.items()}
        return int("".join(str(key[w]) for w in out))

    yield sum(derive(ln[:10], ln[-4:]) for ln in lines)
