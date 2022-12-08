import io

example = [
    "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
    "bvwbjplbgvbhsrlpgdmjqwftvncz",
    "nppdvjthqldpwncqszvftbrmjlhg",
    "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
    "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
]

class Parser:

    def __init__(self, length=4):
        self.buffer = ""
        self.marker_length = length
        self.position = 0

    def update(self, char):
        self.position += 1
        found = self.buffer.find(char)
        if found == -1:
            self.buffer = self.buffer + char
            if len(self.buffer) == self.marker_length:
                return self.position
        else:
            self.buffer = self.buffer[found+1:] + char

    @staticmethod
    def run(f, length=4):
        p = Parser(length)
        while True:
            c = f.read(1)
            if not c:
                return
            xx = p.update(c)
            if xx:
                return xx

def test():
    return [Parser.run(io.StringIO(s)) for s in example]


def task1():
    with open('input') as f:
        return Parser.run(f)

def task2():
    with open('input') as f:
        return Parser.run(f, 14)


