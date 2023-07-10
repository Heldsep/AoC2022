import os
import string


def read_file():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open((os.path.join(__location__, "large_input.txt")), "r")
    return f.read().splitlines()


def create_prios():
    a = {string.ascii_lowercase[i-1]: i for i in range(1, 27)}
    b = {string.ascii_uppercase[i-27]: i for i in range(27, 53)}
    return a | b


def solve_1():
    input = read_file()
    prios = create_prios()
    result = 0
    for line in input:
        comp1 = line[:len(line)//2]
        comp2 = line[len(line)//2:]
        result += prios[''.join(sorted(set(comp1) & set(comp2)))]
    return result


def solve_2():
    input = read_file()
    groups = [input[n:n+3] for n in range(0, len(input), 3)]
    prios = create_prios()
    result = 0
    for group in groups:
        elve1 = group[0]
        elve2 = group[1]
        elve3 = group[2]
        result += prios[''.join(sorted(set(elve1) & set(elve2) & set(elve3)))]
    return result


if __name__ == "__main__":
    print(solve_2())
