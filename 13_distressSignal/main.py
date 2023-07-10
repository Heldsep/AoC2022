import os
import string
import re


SMALL = True


def read_file():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    if SMALL:
        f = open((os.path.join(__location__, "small_input.txt")), "r")
    else:
        f = open((os.path.join(__location__, "large_input.txt")), "r")
    return f.read()


def parse_comparisons(input):
    partial = [y for x in input.split('\n\n') for y in x.splitlines()]
    return [partial[i:i+2] for i in range(0, len(partial), 2)]


def eval_lists(left, right):


def eval_ints(left, right):


def eval_list_int(left, right):


def eval_int_list(left, right):


def parse_packet(packet):
    for (left, right) in pairs:
        for i in range(max(len(left), len(right))):
            match left[i]:
                case '[':
                    if right[i] == '[':
                        eval_lists([left[i:].split(']', 1)[0]])


def solve_1():
    pairs = parse_comparisons(read_file())

    return comparisons


def solve_2():
    return


if __name__ == "__main__":
    print(solve_1())
