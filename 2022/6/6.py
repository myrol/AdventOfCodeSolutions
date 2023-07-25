def main():
    with open("input.txt", "r") as fp:
        datastream = fp.read()

    message_len = 14
    i = 0
    while len(set(datastream[i:i+message_len])) != message_len:
        i += 1
    print(i+message_len)


if __name__ == "__main__":
    main()