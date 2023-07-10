import os
import sys

SMALL = False


def read_file():
    __location__ = os.path.realpath(os.path.join(
        os.getcwd(), os.path.dirname(__file__)))
    if SMALL:
        f = open((os.path.join(__location__, "small_input.txt")), "r")
    else:
        f = open((os.path.join(__location__, "large_input.txt")), "r")
    return f.read()


def check(st, div):
    n = len(st)

    # Compute sum of even and odd digit
    # sums
    oddDigSum = 0
    evenDigSum = 0
    for i in range(0, n):
        # When i is even, position of digit is odd
        if (i % 2 == 0):
            oddDigSum = oddDigSum + ((int)(st[i]))
        else:
            evenDigSum = evenDigSum + ((int)(st[i]))

    # Check its difference is divisible by div or not
    return ((oddDigSum - evenDigSum) % div == 0)


def parse_monkey(monkeys):
    result = []
    for monkey in monkeys:
        data = {}
        data['inspections'] = 0
        data['items'] = monkey.split('items: ')[1].split('\n', 1)[
            0].split(', ')
        a, op, b = [x for x in monkey.split('Operation: new = ')[
            1].split('\n', 1)[0].split(' ')]
        data['operation'] = (a, op, b)
        test = int(monkey.split('Test: ')[1].split(
            '\n', 1)[0].rsplit(' ', 1)[1])
        true = int(monkey.split('If true')[1].split(
            '\n', 1)[0].rsplit(' ', 1)[1])
        false = int(monkey.split('If false')[1].split(
            '\n', 1)[0].rsplit(' ', 1)[1])
        data['test'] = (test, true, false)
        result.append(data)
    return result


def parse_input(input):
    segments = input.split('\n\n')
    monkeys = []
    for seg in segments:
        monkeys.append(seg)
    return parse_monkey(monkeys)


def solve_1():
    monkeys = parse_input(read_file())
    for round in range(20):
        for m in monkeys:
            # for item in m['items']:
            while m['items']:
                item = m['items'].pop(0)
                worry = eval(" ".join(
                    [str(item) for item in [item if x == 'old' else x for x in m['operation']]]))
                m['inspections'] += 1
                bored = worry//3
                if check(str(bored), m['test'][0]):
                    monkeys[m['test'][1]]['items'].append(bored)
                else:
                    monkeys[m['test'][2]]['items'].append(bored)
    inspects = [m['inspections'] for m in monkeys]
    inspects.sort()
    a, b = inspects[-2:]
    print(a, b)
    return a * b


def reduce(number):
    holy_number = 9699690
    # holy_number = 96577
    if number > holy_number:
        number = number % holy_number
    return number


def solve_2():
    monkeys = parse_input(read_file())
    print(monkeys)
    for round in range(10000):
        for m in monkeys:
            while m['items']:
                item = m['items'].pop(0)
                worry = eval(" ".join(
                    [str(item) for item in [item if x == 'old' else x for x in m['operation']]]))
                m['inspections'] += 1
                worry = reduce(worry)
                if worry % m['test'][0] == 0:
                    monkeys[m['test'][1]]['items'].append(worry)
                else:
                    monkeys[m['test'][2]]['items'].append(worry)
    inspects = [m['inspections'] for m in monkeys]
    inspects.sort()
    a, b = inspects[-2:]
    print(a, b)
    return a * b


if __name__ == "__main__":
    print(solve_2())
