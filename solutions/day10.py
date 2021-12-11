def solve(data, log):
    m = {"(": ")", "[": "]", "{": "}", "<": ">"}
    pa = {")": 3, "]": 57, "}": 1197, ">": 25137}
    pb = {")": 1, "]": 2, "}": 3, ">": 4}
    sa, sb = 0, []
    for line in data.splitlines():
        buf = []
        for c in line:
            if c in m:
                buf.append(c)
            elif m[buf.pop()] != c:
                sa += pa[c]
                break
        else:
            p = 0
            for c in buf[::-1]:
                p = p * 5 + pb[m[c]]
            sb.append(p)
    yield sa
    yield sorted(sb)[len(sb) // 2]
