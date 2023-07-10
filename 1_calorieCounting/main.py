import os

def read_file():
    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open((os.path.join(__location__, "large_input.txt")), "r")
    return f.read()

def solve_1():
    input = read_file()
    elves = input.split('\n\n')
    total_calories = []
    for elve in elves:
        calories = elve.split('\n')
        total_calories.append(sum([int(c) for c in calories]))
    return max(total_calories)

def solve_2():
    input = read_file()
    elves = input.split('\n\n')
    total_calories = []
    for elve in elves:
        calories = elve.split('\n')
        total_calories.append(sum([int(c) for c in calories]))
    total_calories.sort()
    return(sum(total_calories[-3:]))

if __name__ == "__main__":
    print(solve_2())
