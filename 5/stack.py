import io

example = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

def read_stack(f):
    layers = []
    while True:
        line = f.readline()
        if not line.strip():
            return layers[:-1]
        explode = [x for x in line[1::4]]
        layers.append(explode)

def to_stacks(layers):
    result = []
    for i in range(0, len(layers[0])):
        stack = ''.join((x[i] for x in layers)).strip()
        result.append(stack)
    return result

def read_move(line):
    (move_word, number, from_word, source, to_word, target) = line.split()
    return (int(number), int(source), int(target))

def do_move_9000(stacks, move):
    number, source, target = move
    reversed_batch = stacks[source-1][:number][::-1]
    stacks[source-1] = stacks[source-1][number:]
    stacks[target-1] = reversed_batch + stacks[target-1]

def do_move_9001(stacks, move):
    number, source, target = move
    batch = stacks[source-1][:number]
    stacks[source-1] = stacks[source-1][number:]
    stacks[target-1] = batch + stacks[target-1]

def first_or_space(s):
    return s[0] if len(s) > 0 else ' '

def run_program(sio, move_function):
    layers = read_stack(sio)
    print(layers)
    stacks = to_stacks(layers)
    print(stacks)
    move_line = "move 3 from 1 to 3"
    move = read_move(move_line)
    print(move)
    print('*****')
    while True:
        print(stacks)
        move_line = sio.readline().strip()
        if not move_line:
            break
        move = read_move(move_line)
        print(move)
        move_function(stacks, move)
    print(stacks)
    tops = (first_or_space(x) for x in stacks)
    print(''.join(tops))
    

def test(move_function):
    run_program(io.StringIO(example), move_function)

def task1():
    with open('input') as f:
        run_program(f, do_move_9000)

def task2():
    with open('input') as f:
        run_program(f, do_move_9001)
