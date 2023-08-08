def main():
    with open("input.txt", "r") as fp:
        input = fp.readlines()

    part_one(input)


def part_one(instructions):
    x = 1
    cycle = 1
    sum_signal_strengths = 0
    crt = ""

    def do_cycle(n):
        nonlocal x, cycle, sum_signal_strengths, sprite_range, crt, instr
        # print()
        for i in range(n):
            # print(f"Cycle {cycle}")
            # print(f"Sprite at: {x}, Pointer at: {len(crt.strip())}")
            # print(f"CRT: {crt.strip()}")
            if (cycle - 20) % 40 == 0:
                sum_signal_strengths += x * cycle
            if len(crt) % 41 in sprite_range:
                crt += "H"
            else:
                crt += " "
            if cycle % 40 == 0:
                crt += "\n"
            cycle += 1

    for instr in instructions:
        instr = instr.strip().split(" ")
        sprite_range = range(x-1, x+2)
        if instr[0] == "addx":
            do_cycle(2)
            x += int(instr[1])
        elif instr[0] == "noop":
            do_cycle(1)
    print(f"Sum of signal strengths: {sum_signal_strengths}")
    print(crt)


if __name__ == "__main__":
    main()