def getLines(file):
    with open(file) as file:
        lines = [line.rstrip() for line in file]
    return lines

def solve():

    # Get each lines splitted: [["1","2"], ["3","4"]]
    lines = [levels.split(" ") for levels in getLines("input.txt")]
    # Convert each reports to int: [[1,2], [3,4]]
    reports = [[int(x) for x in rep] for rep in lines]
    # List of deltas [[-1], [-1]]
    deltas = [[i-k for i,k in zip(report[0::1], report[1::1])] for report in reports]
    # For each list of deltas, check if they have the same sign and between 1 and 3
    safes = [
            all(x >= 0 and 1 <= abs(x) <= 3 for x in deltas) or
            all(x <= 0 and 1 <= abs(x) <= 3 for x in deltas)
            for deltas in deltas
        ].count(True)
    print(safes)

solve()