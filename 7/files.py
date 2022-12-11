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


def test_unread():
    sio = Unread(io.StringIO("abc\ndef\n123"), "blabla\n")
    while True:
        line = sio.readline()
        if not line:
            break
        print(line.strip())


def parse_listing_line(line):
    try:
        (x, y) = line.strip().split()
        if x == 'dir':
            return (x, y)
        return ('file', int(x), y)
    except ValueError:
        pass


def summarize(files, dirs):
    return sum((size for (size, _) in files))
    +sum((size for (size, _) in dirs))


def read_listing(f):
    files = []
    dirs_todo = set()
    dirs = []
    while True:
        line = f.readline()
        if not line:
            return (files, dirs)
        thing = parse_listing_line(line)
        if not thing:
            f.unread(line)
            (name, listing) = read_dir(f)
            dirs_todo.remove(name)
            dirs.add((name, summarize(*listing)))
        else:
            (type_of_thing, *info) = thing
            if type_of_thing == 'file':
                files.append(info)
            elif type_of_thing == 'dir':
                dirs_todo.add(thing)


def read_dir(sio):
    line = sio.readline()
    (_, _, name) = line.strip().split()  # $ cd a
    _ = sio.readline()  # $ ls
    return (name, read_listing(sio))


def reader2():
    sio = Unread(io.StringIO(example))
    print(read_dir(sio))
