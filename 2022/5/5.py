def main():
    with open("input.txt", "r") as fp:
        input = fp.readlines()

    solution(input)


def solution(input):
    stacks_len = int((len(input[0])+1)/4)
    stacks = list()
    for i in range(stacks_len):
        stacks.append(list())

    initiate_stacks = True
    for line in input:
        if line[0] == "\n":
            initiate_stacks = False
            continue
        if initiate_stacks:
            for i in range(0, len(line), 4):
                stack_index = int(i/4)
                letter = line[i+1]
                if letter.isspace():
                    continue
                stacks[stack_index].insert(0, letter)
        else:
            n, f, t = sanitizeCommand(line)
            # PART ONE
            # for i in range(n):
            #     stacks[t].append(stacks[f].pop())

            # PART TWO
            multiple_crates = stacks[f][-n:]
            stacks[t].extend(multiple_crates)  # PART TWO
            for i in range(n):
                stacks[f].pop()
    output = ""
    for i, stack in enumerate(stacks):
        output += stack[-1]
    print(output)

def sanitizeCommand(s):
    line = s[5:]
    numerator, line = line.split(" from ")
    from_stack, to_stack = line.split(" to ")
    numerator, from_stack, to_stack = int(numerator), int(from_stack)-1, int(to_stack)-1
    return numerator, from_stack, to_stack


if __name__ == "__main__":
    main()