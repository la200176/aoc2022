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

def process_input(line, location):
    (dollar, cmd, *args) = line.split()
    if cmd == "cd":
        (where, ) = args
        if where == '..':
            return (location[:-1], None)
        else:
            return (location + args, None)
    elif cmd == "ls":
        return (location, None)
    raise ValueError(f"cant process '{line}'")

def next_or_last_line(f, last_line=None):
    if last_line:
        return last_line
    line = f.readline()
    if line:
        return line.strip()

def test():
    sio = io.StringIO(example)
    location = []
    old_line = None
    while True:
        line = next_or_last_line(sio, old_line)
        if not line:
            break
        try:
            (new_location, old_line) = process_input(line, location)
        except ValueError as ve:
            msg = f"ERR {ve}"
        else:
            msg = "OK"
            location = new_location
        print(f"{line.ljust(30)} #{location} {msg}")


test()
