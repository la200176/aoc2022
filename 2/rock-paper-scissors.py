import sys

ABC = "Rock Paper Scissors"
XYZ = "Rock Paper Scissors"

shapes = {
    "A": "Rock",
}


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

if __name__ == '__main__':
    total = 0
    for line in sys.stdin.readlines():
        round = scores[line.strip()]
        print(f"{line.strip()} {round}")
        total += round
    print(f"score {total}")
