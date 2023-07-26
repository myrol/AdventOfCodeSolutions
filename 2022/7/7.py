import string


class File:
    def __init__(self, name, size=0, parent=None):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = list()

    def add_child(self, child):
        self.children.append(child)
        self.size += child.size

    def update_size(self):
        self.size = 0 if len(self.children) > 0 else self.size
        for child in self.children:
            child.update_size()
            self.size += child.size

    def get_child(self, child_name):
        return list(filter(lambda c: c.name == child_name, self.children))[0]


def main():
    with open("input.txt", "r") as fp:
        terminal_history = fp.readlines()

    root = parse_history(terminal_history)
    root.update_size()
    print(sum_sizes_less_than(root, 100000))
    print(closest_dir_to2(root, root.size - (70000000 - 30000000)))

def sum_sizes_less_than(root, threshold):
    sum = 0
    if root.size < threshold:
        sum += root.size

    for child in root.children:
        if len(child.children) > 0:
            sum += sum_sizes_less_than(child, threshold)
    return sum


def closest_dir_to2(root, threshold):
    def helper_recursion(f, t, _sizes):
        for child in f.children:
            if len(child.children) > 0 and threshold < child.size:
                _sizes.append(child.size)
                helper_recursion(child, t, _sizes)

    sizes = [root.size]
    helper_recursion(root, threshold, sizes)
    return min(sizes)

def closest_dir_to(root, threshold):
    closest_size = root.size
    for child in root.children:
        if len(child.children) > 0:
            if threshold < child.size < closest_size:
                closest_size = closest_dir_to(child, threshold)
    return closest_size


def parse_history(history):
    root = File(name="/", size=0)
    root.parent = root
    current = root
    for line in history:
        line = line.strip().split(" ")
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    current = root
                elif line[2] == "..":
                    current = current.parent
                else:
                    current = current.get_child(line[2])
            else:
                continue
        else:
            if line[0] == "dir":
                file = File(name=line[1], size=0, parent=current)
            else:
                file = File(name=line[1], size=int(line[0]), parent=current)
            current.add_child(file)
    return root


if __name__ == "__main__":
    main()