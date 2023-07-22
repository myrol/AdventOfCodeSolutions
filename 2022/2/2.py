LOSS = 0
DRAW = 3
WIN = 6


def main():
    with open('input.txt', 'r') as fp:
        rounds = fp.readlines()

    total_score = 0
    for r in rounds:
        my_symbol = get_symbol(r[0], r[2])
        total_score += get_result(r[0], my_symbol)
    print(f"Total score: {total_score}")


def get_result(opponent, me):
    round_result = 0
    if get_value(opponent) == get_value(me):
        round_result += DRAW
    if opponent == 'A' and me == 'Y':
        round_result += WIN
    if opponent == 'A' and me == 'Z':
        round_result += LOSS
    if opponent == 'B' and me == 'X':
        round_result += LOSS
    if opponent == 'B' and me == 'Z':
        round_result += WIN
    if opponent == 'C' and me == 'X':
        round_result += WIN
    if opponent == 'C' and me == 'Y':
        round_result += LOSS

    round_result += get_value(me)
    return round_result


def get_value(symbol):
    match symbol:
        case 'A':
            return 1
        case 'X':
            return 1
        case 'B':
            return 2
        case 'Y':
            return 2
        case 'C':
            return 3
        case 'Z':
            return 3


def get_symbol(opponent, strategy):
    match strategy:
        case 'X':
            match opponent:
                case 'A': return 'Z'
                case 'B': return 'X'
                case 'C': return 'Y'
        case 'Y':
            match opponent:
                case 'A': return 'X'
                case 'B': return 'Y'
                case 'C': return 'Z'
        case 'Z':
            match opponent:
                case 'A': return 'Y'
                case 'B': return 'Z'
                case 'C': return 'X'


if __name__ == '__main__':
    main()
