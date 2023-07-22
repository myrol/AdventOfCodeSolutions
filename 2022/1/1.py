def main():
    with open('input.txt', 'r') as fp:
        lines = fp.readlines()

    most_calories = 0
    current_calories_total = 0
    for line in lines:
        if line != '\n':
            current_calories_total += int(line)
            continue
        if current_calories_total > most_calories:
            most_calories = current_calories_total
        current_calories_total = 0

    print(most_calories)


if __name__ == '__main__':
    main()
