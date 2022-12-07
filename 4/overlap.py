example = [
    "2-4,6-8",
    "2-3,4-5",
    "5-7,7-9",
    "2-8,3-7",
    "6-6,4-6",
    "2-6,4-8"
]

def parse_range(s):
    return [int(x) for x in s.split("-")]

def parse_line(l):
    return [parse_range(x) for x in l.split(',')]

def left_covers(r1, r2):
    (start1, end1) = r1
    (start2, end2) = r2
    return start1 <= start2 and end1 >= end2

def covering(r1, r2):
    return left_covers(r1, r2) or left_covers(r2, r1)

def covering_pair(line):
    r1, r2 = parse_line(line)
    return covering(r1, r2)

def left_overlaps(r1, r2):
    (start1, end1) = r1
    (start2, end2) = r2
    return start2 >= start1 and start2 <= end1 or end2 >= start1 and end2 <= end1

def overlapping(r1, r2):
    return left_overlaps(r1, r2) or left_overlaps(r2, r1)

def overlapping_pair(line):
    r1, r2 = parse_line(line)
    return overlapping(r1, r2)

def task1():
    with open('input') as f:
        result = sum((int(covering_pair(x)) for x in f.readlines()))
    return result

def task2():
    with open('input') as f:
        result = sum((int(overlapping_pair(x)) for x in f.readlines()))
    return result

