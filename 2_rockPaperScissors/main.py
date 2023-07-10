import os

SCORES = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
    'loss': 0,
    'draw': 3,
    'win': 6
}

MY_HAND = {
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors'
}

OPPONENT_HAND = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors'
}

OUTCOME = {
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win'
}


def read_file():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open((os.path.join(__location__, "large_input.txt")), "r")
    return f.read().splitlines()


def play_1(me, opponent):
    result = 0
    match me:
        case 'rock':
            result += SCORES['rock']
            match opponent:
                case 'rock':
                    return SCORES['draw'] + result
                case 'paper':
                    return SCORES['loss'] + result
                case 'scissors':
                    return SCORES['win'] + result
        case 'paper':
            result += SCORES['paper']
            match opponent:
                case 'rock':
                    return SCORES['win'] + result
                case 'paper':
                    return SCORES['draw'] + result
                case 'scissors':
                    return SCORES['loss'] + result
        case 'scissors':
            result += SCORES['scissors']
            match opponent:
                case 'rock':
                    return SCORES['loss'] + result
                case 'paper':
                    return SCORES['win'] + result
                case 'scissors':
                    return SCORES['draw'] + result


def play_2(outcome, opponent):
    result = 0
    match outcome:
        case 'loss':
            result += SCORES['loss']
            match opponent:
                case 'rock':
                    return SCORES['scissors'] + result
                case 'paper':
                    return SCORES['rock'] + result
                case 'scissors':
                    return SCORES['paper'] + result
        case 'win':
            result += SCORES['win']
            match opponent:
                case 'rock':
                    return SCORES['paper'] + result
                case 'paper':
                    return SCORES['scissors'] + result
                case 'scissors':
                    return SCORES['rock'] + result
        case 'draw':
            result += SCORES['draw']
            match opponent:
                case 'rock':
                    return SCORES['rock'] + result
                case 'paper':
                    return SCORES['paper'] + result
                case 'scissors':
                    return SCORES['scissors'] + result


def solve_1():
    input = read_file()
    result = 0
    for line in input:
        hands = line.split(' ')
        opponent = OPPONENT_HAND[hands[0]]
        me = MY_HAND[hands[1]]
        result += play_1(me, opponent)
    return result


def solve_2():
    input = read_file()
    result = 0
    for line in input:
        data = line.split(' ')
        opponent = OPPONENT_HAND[data[0]]
        outcome = OUTCOME[data[1]]
        result += play_2(outcome, opponent)
    return result


if __name__ == "__main__":
    print(solve_2())
