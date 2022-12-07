example = [
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
]


def priority(letter):
    if letter >= 'a' and letter <= 'z':
        return ord(letter) - ord('a') + 1
    if letter >= 'A' and letter <= 'Z':
        return ord(letter) - ord('A') + 27
    raise ValueError(f"letter must be a-zA-Z, got {letter}")


def letter(priority):
    if priority >= 27 and priority <= 52:
        return chr(priority + ord('A') - 27)
    if priority >= 1 and priority <= 26:
        return chr(priority + ord('a') - 1)
    raise ValueError(f"priority must be in [1, 52], got {priority}")


class Rucksack:

    def __init__(self, rucksack_list):
        self.compartment1 = [0] * 52
        self.compartment2 = [0] * 52
        self.parse_list(rucksack_list)

    @staticmethod
    def letter_index(letter):
        return priority(letter) - 1

    def parse_list(self, rucksack_list):
        middle = len(rucksack_list) // 2
        for letter in rucksack_list[:middle]:
            self.compartment1[Rucksack.letter_index(letter)] += 1
        for letter in rucksack_list[middle:]:
            self.compartment2[Rucksack.letter_index(letter)] += 1

    def show(self):
        for (i, x) in enumerate(self.compartment1):
            if x > 0:
                print(f"{letter(i + 1)} {x}")
        print('--')
        for (i, x) in enumerate(self.compartment2):
            if x > 0:
                print(f"{letter(i + 1)} {x}")

    def find_duplicate(self):
        for (i, (c1, c2)) in enumerate(zip(self.compartment1, self.compartment2)):
            if c1 * c2 > 0:
                return (i + 1, letter(i + 1))

def task1():
    result = 0
    with open('input') as f:
        result += sum(x for (x, _) in [Rucksack(x.strip()
                                                ).find_duplicate() for x in f.readlines()])
    return result
    