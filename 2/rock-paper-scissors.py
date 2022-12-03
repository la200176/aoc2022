import sys



order = "rock > scissors > paper > rock"
shape_score = "1 2 3"
round_score = {
    "loose": 0,
    "draw": 3,
    "win": 6
}



scores = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,

    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,

    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3
}

XYZ_2 = "lose draw win"

ABC = "Rock Paper Scissors"
XYZ = "Rock Paper Scissors"


translate = {
    "A X": "A Z",
    "A Y": "A X",
    "A Z": "A Y",

    "B X": "B X",
    "B Y": "B Y",
    "B Z": "B Z",

    "C X": "C Y",
    "C Y": "C Z",
    "C Z": "C X"
}

if __name__ == '__main__':
    total = 0
    total2 = 0
    for line in sys.stdin.readlines():
        line = line.strip()
        round = scores[line]
        round2 = scores[translate[line]]
        print(f"{line} {round} {translate[line]} {round2}")
        total += round
        total2 += round2
    print(f"score {total} score, part2: {total2}")
