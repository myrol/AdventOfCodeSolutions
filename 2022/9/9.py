import math

def main():
    with open("input.txt", "r") as fp:
        input = fp.readlines()

    print(n_visited(input))


def n_visited(input):
    """
    Works by checking if a node is more than sqrt(2) away from the previous node after moving and applies
    a vector according to the direction the previous node moved.

    +++    +++    +++
    TH+ -> T+H -> +TH Here the vector would be (1, 0)
    +++    +++    +++

    +++    +++    +++
    +H+ -> ++H -> +TH Here the vector would be (1, 1)
    T++    T++    +++

    This vector is calculated based on the distance to the previous node (H is first, T is next).
    Here the actual vector would be (2, 1) in the second step. I reduce this vector to only allow 0s or 1s.
    So (2, 1) becomes (1, 1)

    Similarly, a vector like (-2, -2) would become (-1, 1), which corresponds to the rules
    of movement stated in the puzzle.

    :param input:
    :return:
    """
    sequences = sanitize(input)
    rope = [(0, 0)] * 10
    unique_visits = {(0, 0)}
    max_dist = math.sqrt(2)
    for seq in sequences:
        direction, quantity = seq
        for i in range(quantity):
            print_console(rope)
            rope[0] = calc_new_pos(rope[0], direction)
            for j in range(1, len(rope)):
                dist = distance(rope[j-1], rope[j])
                if dist > max_dist:
                    dx, dy = norm_vector(rope[j - 1], rope[j])
                    rope[j] = (rope[j][0] + dx, rope[j][1] + dy)
                if j == len(rope)-1:
                    unique_visits.add(rope[j])
    return len(unique_visits)

def norm_vector(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]

    dx = 0 if dx == 0 else int(dx/abs(dx))
    dy = 0 if dy == 0 else int(dy/abs(dy))
    return dx, dy


def distance(head, tail):
    return math.sqrt((head[0]-tail[0])**2 + (head[1]-tail[1])**2)

def calc_new_pos(bodypart, direction):
    match direction:
        case "R": direction = (1, 0)
        case "D": direction = (0, -1)
        case "L": direction = (-1, 0)
        case "U": direction = (0, 1)
    return bodypart[0]+direction[0], bodypart[1]+direction[1]


def print_console(coordinates):
    x_coords = [x for x, _ in coordinates]
    y_coords = [y for _, y in coordinates]
    x_min, x_max = min(x_coords), max(x_coords)
    y_min, y_max = min(y_coords), max(y_coords)
    output = f"Interval: [{x_min}, {x_max}] / [{y_min}, {y_max}]\n"
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            for i, pair in enumerate(coordinates):
                if (x, y) == pair:
                    output += f"{i}"
                    break
            else:
                output += "+"
        output += "\n"
    print(output)


def sanitize(input):
    sequence = list()
    for line in input:
        line = line.strip()
        direction, quantity = line.split(" ")
        sequence.append((direction, int(quantity)))
    return sequence

if __name__ == "__main__":
    main()