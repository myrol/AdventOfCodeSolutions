def main():
    with open('input.txt', 'r') as fp:
        lines = fp.readlines()

    elves = list()
    most_calories = 0
    current_calories_total = 0
    for line in lines:
        if line != '\n':
            current_calories_total += int(line)
            continue
        if current_calories_total > most_calories:
            most_calories = current_calories_total
        elves.append(current_calories_total)
        current_calories_total = 0

    elves.sort(reverse=True)
    print(f"Top Three Elves: {elves[0]}, {elves[1]}, {elves[2]}.\nTotal: {elves[0]+elves[1]+elves[2]}")


if __name__ == '__main__':
    main()
