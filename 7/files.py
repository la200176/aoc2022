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


def parse_listing_line(line):
    try:
        (x, y) = line.strip().split()
        if x == 'dir':
            return ((x, y), True)
        return (('file', int(x), y), True)
    except ValueError:
        return (None, False)


def read_listing(f, parse_line, location=[]):
    result = []
    while True:
        line = f.readline()
        if not line:
            return (result, None)
        (thing, ok) = parse_line(line)
        if not ok:
            f.unread(line)
            new_location = read_command(f, parse_command_line, location)
            print(f"LIS {new_location} {result}")
        else:
            result.append(thing)


def parse_command_line(line):
    (dollar, cmd, *rest) = line.strip().split()
    if dollar == "$":
        if cmd == "cd":
            (target,) = rest
            if target == "..":
                return (lambda x: x[:-1], True)
            else:
                return (lambda x: x + rest, True)
        if cmd == "ls":
            return (lambda x: x, True)
    return (None, False)


def read_command(f, parse_command_line, location=[]):
    while True:
        line = f.readline()
        if not line:
            return (location, None)
        (navigation, ok) = parse_command_line(line)
        if not ok:
            f.unread(line)
            listing = read_listing(f, parse_listing_line, location)
            print(f"CMD {location} {listing}")
        else:
            location = navigation(location)


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


def reader(f):
    sio = Unread(f)
    processor = dict(listing=lambda f: read_listing(f, parse_listing_line),
                     command=lambda f: read_command(f, parse_command_line))
    mode = "command"
    while True:
        (result, line) = processor[mode](sio)
        if not line:
            break
        print(f"{mode}: {result}")
        sio.unread(line)
        if mode == "command":
            mode = "listing"
        elif mode == "listing":
            mode = "command"


def test_listing(x):
    sio = Unread(io.StringIO(x))
    print(read_listing(sio, parse_listing_line))


def test_cmd(x):
    sio = Unread(io.StringIO(x))
    print(read_command(sio, parse_command_line))


def test_unread():
    sio = Unread(io.StringIO("abc\ndef\n123"), "blabla\n")
    while True:
        line = sio.readline()
        if not line:
            break
        print(line.strip())

def test_reader():
    sio = Unread(io.StringIO(example))
    read_command(sio, parse_command_line, [])
