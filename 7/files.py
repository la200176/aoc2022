import io

example = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

list1 = """4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

list2 = """dir e
29116 f
2557 g
62596 h.lst
$ cd e
"""

list3 = """dir a
14848514 b.txt
8504156 c.dat
dir d
"""

cmd1 = """$ cd /
$ ls"""


class Unread:
    def __init__(self, stream):
        self.stream = stream
        self.unread_line = None

    def unread(self, line):
        self.unread_line = line

    def readline(self):
        if self.unread_line:
            unread_line = self.unread_line
            self.unread_line = None
            return unread_line
        return self.stream.readline()

    def next(self):
        result = self.readline()
        if result:
            return result.strip()


def test_unread():
    sio = Unread(io.StringIO("abc\ndef\n123"), "blabla\n")
    while True:
        line = sio.readline()
        if not line:
            break
        print(line.strip())

list4 = """$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def parse_listing(line):
    try: 
        (x, y) = line.split()
        if x == 'dir':
            return (x, y)
        return (int(x), y)
    except ValueError:
        pass
    except AttributeError:
        pass
    

def listing(sio):
    result = []
    while True:
        line = sio.next()
        thing = parse_listing(line)
        if not thing:
            sio.unread(line)
            return result
        result.append(thing)

        
def read_dir(sio, level=0, accu=None):
    accu = accu or []
    line = sio.next()
    (_, _, name) = line.split()
    _ = sio.next()
    content = listing(sio)
    summary = []
    total_size = 0
    for thing in content:
        if thing[0] == 'dir':
            result, size, accu = read_dir(sio, level+1, accu)
            summary.append([thing[0], size, thing[1], result])
            total_size += size
        else:
            summary.append(['file', *thing])
            total_size += thing[0]
    if level > 0:
        _ = sio.next()
    if total_size <= 100000:
        accu.append(total_size)
    return summary, total_size, accu

def test():
    sio = Unread(io.StringIO(example))
    tree, size, found = read_dir(sio)
    print(tree)
    print(size)
    print(sum(found))

def task1():
    with open('input') as f:
        sio = Unread(f)
        tree, size, found = read_dir(sio)
    print(tree)
    print(size)
    print(sum(found))

def task2():
    total_space = 70000000
    needed = 30000000
    with open('input') as f:
        sio = Unread(f)
        tree, size, found = read_dir(sio)
    print(tree)
    print(size)
    print(sum(found))
    unused = total_space - size
    print(f"unused: {unused}")
    threshold = needed - unused
    print(f"to delete: {threshold}")
    result = find_dir(tree, threshold)
    print(result)
    print(f"min dir: {min(result)}")

def find_dir(content, threshold, accu=[]):
    for ((kind, size, name, *content)) in content:
        if kind == 'dir':
            if size > threshold:
                accu.append(size)
            accu = accu + find_dir(*content, threshold)
    return accu

def test2():
    total_space = 70000000
    needed = 30000000
    sio = Unread(io.StringIO(example))
    tree, size, found = read_dir(sio)
    print(tree)
    print(size)
    print(sum(found))
    unused = total_space - size
    print(f"unused: {unused}")
    threshold = needed - unused
    print(f"to delete: {threshold}")
    result = find_dir(tree, threshold)
    print(result)
    print(f"min dir: {min(result)}")
