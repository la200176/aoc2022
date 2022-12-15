example = """30373
25512
65332
33549
35390"""


def to_map(s):
    return [[int(x) for x in list(row)] for row in s.split('\n') if row]


def visible_details(trees, position):
    width = len(trees[0])
    height = len(trees)
    (row, col) = position
    tree_height = trees[row][col]
    left_trees = trees[row][:col]
    right_trees = trees[row][col+1:]
    top_trees = [trees[row][col] for row in range(0, row)]
    bottom_trees = [trees[row][col] for row in range(row+1, height)]
    smaller = lambda x: x < tree_height
    all_smaller = lambda trees: all([smaller(tree) for tree in trees])
    return dict(left=(left_trees, all_smaller(left_trees)),
                right=(right_trees, all_smaller(right_trees)),
                top=(top_trees, all_smaller(top_trees)),
                bottom=(bottom_trees, all_smaller(bottom_trees)))

def visible(trees, position):
    details = visible_details(trees, position)
    return any((x for (_, x) in details.values()))

def test1():
    trees = to_map(example)
    count = 0
    for (row, xx) in enumerate(trees):
        for (col, _) in enumerate(xx):
            count += int(visible(trees, [row, col]))
    return count

def task1():
    with open('input') as f:
        s = f.read()
    trees = to_map(s)
    count = 0
    for (row, xx) in enumerate(trees):
        for (col, _) in enumerate(xx):
            count += int(visible(trees, [row, col]))
    return count