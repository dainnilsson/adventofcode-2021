def solve(data, log):
    def fold_x(ps, nx, ny, v):
        return {(x, y) for x, y in ps if x < v} | {
            (x - 1, y) for y in range(ny) for x in range(nx - v) if (nx - x, y) in ps
        }

    def fold_y(ps, nx, ny, v):
        return {(x, y) for x, y in ps if y < v} | {
            (x, y - 1) for x in range(nx) for y in range(ny - v) if (x, ny - y) in ps
        }

    def fold(ps, nx, ny, f):
        a, n = f.split()[-1].split("=")
        is_x, n = a == "x", int(n)
        fn = fold_x if is_x else fold_y
        return fn(ps, nx, ny, n), (n, ny) if is_x else (nx, n)

    lines = data.splitlines()
    i = lines.index("")
    ps = {(x, y) for x, y in [[int(i) for i in v.split(",")] for v in lines[:i]]}
    folds = lines[i + 1 :]
    ps, (nx, ny) = fold(
        ps, max(x for x, y in ps) + 1, max(y for x, y in ps) + 1, folds.pop(0)
    )
    yield len(ps)

    for f in folds:
        ps, (nx, ny) = fold(ps, nx, ny, f)
    yield "\n".join(
        "".join("#" if (x, y) in ps else "." for x in range(nx)) for y in range(ny)
    )
