def getLines(file):
    with open(file) as file:
        lines = [line.rstrip() for line in file]
    return lines

def solve():
    lines = [line.split("   ") for line in getLines("input.txt")]
    left = [int(x[0]) for x in lines]
    right = [int(x[1]) for x in lines]
    print(sum(x * right.count(x) for x in left))

solve()