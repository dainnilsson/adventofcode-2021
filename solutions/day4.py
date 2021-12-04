def solve(data, log):
    lines = data.splitlines()
    numbers = [int(v) for v in lines.pop(0).split(",")]
    lines = [[int(v) for v in ln.split()] for ln in lines]
    drawn = set(numbers[:4])
    numbers = numbers[4:]

    def row(b, y):
        return lines[b * 6 + y + 1]

    def col(b, x):
        return [row(b, y)[x] for y in range(5)]

    def score(b):
        return sum(v for y in range(5) for v in row(b, y) if v not in drawn)

    def bingo():
        boards = set(range(len(lines) // 6))
        for n in numbers:
            drawn.add(n)
            for b in boards.copy():
                for y in range(5):
                    ln = row(b, y)
                    if n in ln and (
                        all(v in drawn for v in ln)
                        or all(v in drawn for v in col(b, ln.index(n)))
                    ):
                        boards.remove(b)
                        yield score(b) * n

    w = bingo()
    yield next(w)
    *_, last = w
    yield last
