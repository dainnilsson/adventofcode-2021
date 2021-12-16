def solve(data, log):
    ops = {
        0: sum,
        1: lambda x: x[0] if len(x) == 1 else x[0] * ops[1](x[1:]),
        2: min,
        3: max,
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1]),
    }

    def parse(bs):
        v, t, bs = int(bs[:3], 2), int(bs[3:6], 2), bs[6:]
        if t == 4:
            buf = ""
            while bs[0] == "1":
                buf += bs[1:5]
                bs = bs[5:]
            return (v, t, int(buf + bs[1:5], 2)), bs[5:]
        else:
            cs = []
            if bs[0] == "1":
                ns, bs = int(bs[1:12], 2), bs[12:]
                for _ in range(ns):
                    sv, bs = parse(bs)
                    cs.append(sv)
            else:
                tl, bs = int(bs[1:16], 2), bs[16:]
                rl = len(bs) - tl
                while len(bs) > rl:
                    sv, bs = parse(bs)
                    cs.append(sv)
            return (v, t, cs), bs

    r = parse(bin(int(data, 16))[2:].zfill(len(data) * 4))[0]

    def count(v, t, val):
        if t != 4:
            v += sum(count(*s) for s in val)
        return v

    yield count(*r)

    def evaluate(v, t, val):
        if t != 4:
            val = ops[t]([evaluate(*s) for s in val])
        return val

    yield evaluate(*r)
