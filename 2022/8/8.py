def main():
    with open("input.txt", "r") as fp:
        matrix = fp.readlines()

    matrix = [line.strip() for line in matrix]
    global width, height
    width, height = len(matrix[0]), len(matrix)

    n_trees_visible = 0
    scenic_scores = list()
    for i in range(width):
        for j in range(height):
            n_trees_visible += 1 if is_visible(matrix, i, j) else 0
            scenic_scores.append(scenic_score(matrix, i, j))
    print(max(scenic_scores))


def scenic_score(matrix, i, j):
    def walk(_i, _j, di, dj, distance):
        _i, _j = _i+di, _j+dj
        if not(0 <= _i < height and 0 <= _j < width):
            return distance-1
        next_tree = int(matrix[_i][_j])
        if next_tree >= current:
            return distance
        return walk(_i, _j, di, dj, distance+1)
    current = int(matrix[i][j])
    score = walk(i, j, 0, 1, 1)
    score *= walk(i, j, 0, -1, 1)
    score *= walk(i, j, 1, 0, 1)
    score *= walk(i, j, -1, 0, 1)
    return score


def is_visible(matrix, i, j):
    def walk(_i, _j, di, dj):
        _i, _j = _i+di, _j+dj
        if not(0 <= _i < height and 0 <= _j < width):
            return True
        next_tree = int(matrix[_i][_j])
        if next_tree >= current:
            return False
        return walk(_i, _j, di, dj)

    current = int(matrix[i][j])
    visible = walk(i, j, 0, 1)
    if not visible:
        visible = walk(i, j, 0, -1)
    if not visible:
        visible = walk(i, j, 1, 0)
    if not visible:
        visible = walk(i, j, -1, 0)
    return visible



if __name__ == "__main__":
    main()