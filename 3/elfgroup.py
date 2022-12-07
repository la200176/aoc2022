example = [
    [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg"
    ],
    [
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"
    ]

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
        self.compartment = [0] * 52
        self.parse_list(rucksack_list)
    
    @staticmethod
    def letter_index(letter):
        return priority(letter) - 1

    def parse_list(self, rucksack_list):
        for letter in rucksack_list:
            self.compartment[Rucksack.letter_index(letter)] += 1
    
    def show(self):
        for (i, x) in enumerate(self.compartment):
            if x > 0:
                print(f"{letter(i + 1)} {x}")
    
class Group:

    def __init__(self, list1, list2, list3):
        self.rucksack1 = Rucksack(list1)
        self.rucksack2 = Rucksack(list2)
        self.rucksack3 = Rucksack(list3)

    def badge(self):
        for (n, (i1, i2, i3)) in enumerate(zip(self.rucksack1.compartment, 
                                            self.rucksack2.compartment, 
                                            self.rucksack3.compartment)):
            if i1 * i2 * i3 > 0:
                return letter(n+1), n+1


def task2():
    result = 0
    with open('input') as f:
        while True:
            three_lines = [f.readline().strip() for _ in range(3)]
            if not all(three_lines):
                return result
            letter, prio = Group(*three_lines).badge()
            print(f"{','.join(three_lines)}: {letter} {prio} => {result}")
            result += prio
