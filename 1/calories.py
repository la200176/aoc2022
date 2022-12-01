import sys

class Calories:

    def __init__(self):
        self.current_max = None
        self.current_max_elf = None
        self.running_sum = 0
        self.running_elf = 1

    def update(self, number):
        self.running_sum += number

    def next_elf(self):
        if not self.current_max_elf:
            self.current_max_elf = 1
            self.current_max = self.running_sum
            self.running_sum = 0
            self.running_elf = 2
            return
        if self.current_max < self.running_sum:
            self.current_max = self.running_sum
            self.current_max_elf = self.running_elf
        self.running_elf += 1
        self.running_sum = 0


if __name__ == '__main__':
    c = Calories()
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if line == '':
            c.next_elf()
            continue
        try:
            val = int(line)
            c.update(val)
        except:
            continue
    print(f"Elf No {c.current_max_elf} has the most ({c.current_max}) calories in the bag" )