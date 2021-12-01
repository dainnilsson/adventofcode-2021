import os
import pytest
import importlib


@pytest.fixture(scope="session", params=list(range(1, 26)))
def day(request):
    return request.param


@pytest.fixture(scope="session", params=["a", "b"])
def part(request):
    return request.param


@pytest.fixture(scope="session")
def expected(day, part):
    out_f = "output/%d%s.txt" % (day, part)
    if not os.path.isfile(out_f):
        return None

    with open(out_f) as f:
        return f.read()


@pytest.fixture(scope="session")
def solution(day):
    in_f = "input/%d.txt" % day
    if not os.path.isfile(in_f):
        pytest.skip("No input")

    with open(in_f) as f:
        data = f.read()

    module = importlib.import_module("solutions.day%d" % day)
    solver = module.solve(data, lambda *_: None)
    return next(solver), next(solver)


@pytest.fixture(scope="session")
def output(solution, part):
    return solution[0 if part == "a" else 1]


def test_solution(expected, output):
    if expected is None:
        pytest.skip("No output")

    assert "%s\n" % output == expected
