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
    raise ValueError(f"{letter} must be a-zA-Z")


class Rucksack:

    def __init__(self, rucksack_list):
        self.compartment1 = [0] * 52
        self.compartment2 = [0] * 52
        self.parse_list(rucksack_list)


    @staticmethod
    def letter_index(letter):
        return priority(letter) - 1

    def parse_list(self, rucksack_list):
        middle = len(rucksack_list)
        for letter in rucksack_list[:middle]:
            self.compartment1[Rucksack.letter_index(letter)] += 1
        for letter in rucksack_list[middle:]:
            self.compartment2[Rucksack.letter_index(letter)] += 1

    def show(self):
        for (i, x) in enumerate(self.compartment1):
            if x > 0:
                print(f"{chr(i+1)} {x}")
        for (i, x) in enumerate(self.compartment2):
            if x > 0:
                print(f"{chr(i+1)} {x}")
