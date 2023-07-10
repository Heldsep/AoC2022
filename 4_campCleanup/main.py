import os


def read_file():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open((os.path.join(__location__, "large_input.txt")), "r")
    return f.read().splitlines()


def solve_1():
    pairs = read_file()
    result = 0
    for pair in pairs:
        elves = pair.split(',')
        elve1_bounds = [int(x) for x in elves[0].split('-')]
        elve2_bounds = [int(x) for x in elves[1].split('-')]
        elve1 = set(range(elve1_bounds[0], elve1_bounds[1]+1))
        elve2 = set(range(elve2_bounds[0], elve2_bounds[1]+1))
        if elve1.issubset(elve2) or elve2.issubset(elve1):
            result += 1
    return result


def solve_2():
    pairs = read_file()
    result = 0
    for pair in pairs:
        elves = pair.split(',')
        elve1_bounds = [int(x) for x in elves[0].split('-')]
        elve2_bounds = [int(x) for x in elves[1].split('-')]
        elve1 = set(range(elve1_bounds[0], elve1_bounds[1]+1))
        elve2 = set(range(elve2_bounds[0], elve2_bounds[1]+1))
        if elve1.intersection(elve2):
            result += 1
    return result


if __name__ == "__main__":
    print(solve_2())
