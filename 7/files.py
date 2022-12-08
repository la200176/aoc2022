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

class Directory:

    def __init__(self, name):
        self.name = name
        self.files = []
        self.directories = []

    def mkdir(self, name):
        self.directories.append(Directory(name))

    def mkfile(self, file):
        self.files.append(file)
    
    def du(self):
        return sum(x for (_, x) in self.files) + sum(x.du() for x in self.directories)

    def add_line(self, line):
        (number_or_dir, name) = line.split()
        if number_or_dir == 'dir':
            self.mkdir(Directory(name))
        else:
            self.mkfile((name, int(number_or_dir)))

    def plot(self, level=0):
        indent = '--' * level
        print(f"{indent}{self.name}")
        for (name, size) in self.files:
            print(f"{indent}{size} {name}")
        for d in self.directories:
            d.plot(level + 1)


def test():
    d = Directory("/")
    d.plot()
    print('***************************')
    d.mkdir("abc")
    d.mkdir("fgfg")
    d.mkfile(("datei", 100))
    d.mkfile(("d2", 343526))
    d.plot()

test()