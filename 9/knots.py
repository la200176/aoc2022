import io

example = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""


def pull(head_pos, tail_pos):
    (dx, dy) = tuple(head-tail for (head, tail) in zip(head_pos, tail_pos))
    r2 = dx**2 + dy**2
    if r2 == 8:
        return (dx // abs(dx), dy // abs(dy))
    if r2 == 5:
        return (dx // abs(dx), dy // abs(dy))
    if r2 == 4:
        return (dx // abs(dx) if abs(dx) > 0 else 0, dy // abs(dy) if abs(dy) > 0 else 0)
    if r2 == 2:
        return (0, 0)
    if r2 == 1:
        return (0, 0)
    if r2 == 0:
        return (0, 0)
    raise ValueError(f"impossible: head {head_pos}, tail {tail_pos}")


motion = dict(U=(0, 1), D=(0, -1), R=(1, 0), L=(-1, 0))


class State:

    def __init__(self, n=1):
        self.head = (0, 0)
        self.tail = [(0, 0)] * n
        self.visited = dict()
        self.visited[self.tail[-1]] = 1

    def move(self, line):
        (direction, distance) = line.split()
        delta = motion[direction]
        for _ in range(int(distance)):
            self.head = tuple(self.head[i] + delta[i] for i in (0, 1))
            for (n, tail) in enumerate(self.tail):
                head = self.head if n == 0 else self.tail[n-1]
                tail_delta = pull(head, tail)
                self.tail[n] = tuple(tail[i] + tail_delta[i] for i in (0, 1))
            self.visited[self.tail[-1]
                         ] = self.visited.get(self.tail[-1], 0) + 1


def test1():
    sio = io.StringIO(example)
    s = State()
    for line in sio.readlines():
        s.move(line.strip())
    return s.visited


def task1():
    s = State()
    with open('input') as f:
        for line in f.readlines():
            s.move(line.strip())
    return s.visited


def task2(n=1):
    s = State(n=n)
    with open('input') as f:
        for line in f.readlines():
            print(f"{s.head} {s.tail} {line.strip()}")
            s.move(line.strip())
    return s.visited

def test3():
    s = State(2)
    s.head, s.tail = (-11, -6), [(-11, -7), (-12, -8)]
    print(f"{s.head} {s.tail}")
    s.move("R 1")
    print(f"{s.head} {s.tail}")
    s.move("R 1")

test3()
