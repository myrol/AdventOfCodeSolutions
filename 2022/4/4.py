def main():
    with open("input.txt", "r") as fp:
        sections = fp.readlines()

    print(part_one(sections))
    print(part_two(sections))


def fetch_interval(line):
    if "\n" in line:
        line = line[:-1]
    f, s = line.split(",")
    f_start, f_end = f.split("-")
    s_start, s_end = s.split("-")
    f_result = [int(f_start), int(f_end)]
    s_result = [int(s_start), int(s_end)]

    return f_result, s_result


def part_one(sections):
    sum_containments = 0
    for line in sections:
        first_interval, second_interval = fetch_interval(line)
        real_interval = [min(first_interval[0], second_interval[0]), max(first_interval[-1], second_interval[-1])]

        # If one interval contains the other, the min-max interval will be one of the two intervals
        if real_interval == first_interval or real_interval == second_interval:
            sum_containments += 1
    return sum_containments


def part_two(sections):
    sum_containments = 0
    for line in sections:
        first_interval, second_interval = fetch_interval(line)

        real_interval_len = abs(min(first_interval[0], second_interval[0]) - max(first_interval[-1], second_interval[-1]))
        compact_interval_len = abs(first_interval[-1] - first_interval[0]) + abs(second_interval[-1] - second_interval[0])

        # if the distance between the min and max is greater than the length of the interval, they overlap
        if real_interval_len <= compact_interval_len:
            sum_containments += 1
    return sum_containments


if __name__ == '__main__':
    main()