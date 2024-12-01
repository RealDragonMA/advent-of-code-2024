def getLines(file):
    with open(file) as file:
        lines = [line.rstrip() for line in file]
    return lines

def solve():
    lines = [line.split("   ") for line in getLines("input.txt")]
    left = [int(x[0]) for x in lines]
    right = [int(x[1]) for x in lines]
    totalDistance = 0
    while(len(left) != 0 or len(right) != 0):
        minL, minR = min(left), min(right)
        totalDistance += abs(minL - minR)
        left.remove(minL)
        right.remove(minR)

    print(totalDistance)


solve()