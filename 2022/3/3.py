def main():
    with open('input.txt', 'r') as fp:
        lines = fp.readlines()

    sum_prio = 0
    i = 0
    while i < len(lines):
        sum_prio += get_priority(find_duplicate2(lines[i], lines[i+1], lines[i+2]))
        i += 3

    #for line in lines:
    #    sum_prio += get_priority(find_duplicate(line))
    print(sum_prio)


def find_duplicate(rucksack):
    first_compartment = rucksack[:int(len(rucksack)/2)]
    second_compartment = rucksack[int(len(rucksack)/2):]

    symbol_dict = set()
    for f in first_compartment:
        symbol_dict.add(f)

    for s in second_compartment:
        if s in symbol_dict:
            return s

    return None


def find_duplicate2(r1, r2, r3):
    dupes = set()
    for x in r1:
        dupes.add(x)
    re_dupe = set()
    for x in r2:
        if x in dupes:
            re_dupe.add(x)
    dupes = re_dupe
    for x in r3:
        if x in dupes:
            return x


def get_priority(symbol):
    value = ord(symbol)-96
    if value < 0:
        value += 32+26
    return value


if __name__ == '__main__':
    main()