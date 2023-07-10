import os
import numpy as np


def read_file():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open((os.path.join(__location__, "large_input.txt")), "r")
    return f.read()


def parse_cargo(input):
    levels = (input.rsplit(']', 1)[0]+']').splitlines()
    levels.reverse()
    no_levels = int((len(levels[0]) + 1)/4)
    offset = 1
    size = 4
    stacks = [[] for x in range(no_levels)]
    for level in levels:
        cargos = [level[offset+i*size] for i in range(no_levels)]
        for index, cargo in enumerate(cargos):
            if cargo != " ":
                stacks[index].append(cargo)
    return stacks


def parse_ops(input):
    oplines = (input.split('\n\n')[1]).splitlines()
    ops = []
    for opline in oplines:
        split = opline.split(' ')
        quantity = int(split[1])
        src = int(split[3])
        dest = int(split[5])
        ops.append([quantity, src-1, dest-1])
    return ops


def solve_1():
    input = read_file()
    stacks = parse_cargo(input)
    ops = parse_ops(input)
    for [quantity, src, dest] in ops:
        for i in range(quantity):
            moving = stacks[src].pop()
            stacks[dest].append(moving)
    result = ''.join([x.pop() for x in stacks])
    return result


def solve_2():
    input = read_file()
    stacks = parse_cargo(input)
    ops = parse_ops(input)
    for [quantity, src, dest] in ops:
        moving = stacks[src][-quantity:]
        stacks[src] = stacks[src][:-quantity]
        stacks[dest] = stacks[dest] + moving
    result = ''.join([x.pop() for x in stacks])
    return result


if __name__ == "__main__":
    print(solve_2())
