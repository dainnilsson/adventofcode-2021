import argparse
import importlib
import time
import sys
import os


def solve_part(gen, label):
    start = time.time()
    answer = next(gen)
    end = time.time()

    if answer is None:
        print("%s: No solution" % label)
    else:
        ms = (end - start) * 1000
        print("%s (in %d ms): \033[92m%s\033[0m" % (label, ms, answer))


def solve_day(day, in_file, log):
    module = importlib.import_module("solutions.day%d" % day)
    with open(in_file, "r") as f:
        data = f.read()

    print("\033[93mDay %d\033[0m" % day)
    solver = module.solve(data, log)

    solve_part(solver, "A")
    solve_part(solver, "B")

    try:
        next(solver)
        print("Generator did not stop iterating")
        sys.exit(1)
    except StopIteration:
        pass


def completed_days():
    days = []
    for day in DAYS:
        if os.path.isfile("input/%d.txt" % day):
            days.append(day)
    return days


def get_logger(verbose=False):
    if verbose:
        return print
    else:
        return lambda *_: None


parser = argparse.ArgumentParser()
parser.add_argument(
    "-v", "--verbose", action="store_true", help="run with verbose logging"
)
parser.add_argument("day", type=int, nargs="*", metavar="DAYS")
parser.add_argument(
    "-i",
    "--input",
    type=str,
    nargs="?",
    help="specify a directory for input files (defaults to ./input/) or a "
    "specific file (only when running a single day)",
)


DAYS = list(range(1, 26))


def main():
    args = parser.parse_args()

    log = get_logger(args.verbose)
    log("Logging to stdout.")

    input_f = args.input or "input/"

    if os.path.isfile(input_f):
        if len(args.day) != 1:
            print("Specifying custom input file requires running a single day")
            sys.exit(1)

        day = args.day[0]
        log("Running day %d with input %s" % (day, input_f))
        solve_day(day, input_f, log)
    elif os.path.isdir(input_f):
        days = args.day or completed_days()
        for day in days:
            if day not in DAYS:
                print("Invalid day:", day)
                sys.exit(1)
            solve_day(day, os.path.join(input_f, "%d.txt" % day), log)
    else:
        print("INPUT must be a file or directory")
        sys.exit(1)


if __name__ == "__main__":
    main()
