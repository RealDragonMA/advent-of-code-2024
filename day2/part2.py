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
    safe = 0
    for report in reports:
        if isSafe(report):
            safe += 1
            print("Safe without removing any level")
        else:
            for x in report:
                temp = report.copy()
                temp.remove(x)
                if isSafe(temp):
                    print(f"Safe by removing the level {x}.")
                    safe += 1
                    break
            else:
                print("Unsafe regardless of which level is removed.")
    print(safe)

def isSafe(report):
    deltas = [i-k for i,k in zip(report[0::1], report[1::1])]
    return all(x >= 0 and 1 <= abs(x) <= 3 for x in deltas) or all(x < 0 and 1 <= abs(x) <= 3 for x in deltas)


solve()