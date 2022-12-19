import io

example1 = """noop
addx 3
addx -5"""

[1, #noop 
1, #addx 3 start
1, #addx 3 process
4, #addx -5 start
4, #addx -5 process
-1]

def processor(f):
    x = 1
    delay = 0
    add_value = 0
    while True:
        if delay == 0:
            x += add_value
            line = f.readline()
            if not line:
                break
            (cmd, *args) = line.split()
            if cmd == "noop":
                add_value = 0
                delay = 0
            elif cmd == "addx":
                add_value = int(args[0])
                delay = 1
        else:
            delay -= 1
        yield x
    yield x

def test():
    sio = io.StringIO(example1)
    for x in processor(sio):
        print(x)

example = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

def test2():
    sio = io.StringIO(example)
    for (n, x) in enumerate(processor(sio)):
        cycle = n + 1
        print(f"{cycle} {x} {cycle*x}")

def test3():
    sio = io.StringIO(example)
    start = 20
    increment = 40
    for (n, x) in enumerate(processor(sio)):
        cycle = n + 1
        print(f"{cycle} {x} {cycle*x}")
        if cycle % increment == start:
            yield cycle*x

def task1():
    with open('input') as sio:
        start = 20
        increment = 40
        for (n, x) in enumerate(processor(sio)):
            cycle = n + 1
            print(f"{cycle} {x} {cycle*x}")
            if cycle % increment == start:
                yield cycle*x

def task2():
    with open('input') as sio:
        row = []
        for (n, x) in enumerate(processor(sio)):
            cycle = n + 1
            crt = n % 40
            sprite_start = x-1
            sprite_end = x+1
            pixel = '#' if crt >= sprite_start and crt <= sprite_end else ' '
            crt_row = n // 40
            if cycle % 40 == 0:
                print(''.join(row))
                row = []
            else:
                row.append(pixel)
            
