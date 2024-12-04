import re

def getLines(file):
    with open(file) as file:
        lines = [line.rstrip() for line in file]
    return lines

def solve():
    lines = getLines("./input.txt")

    # VerticalLines
    verticalLines = [[lines[i][j] for i in range(len(lines))] for j in range(len(lines[0]))]
    verticalLines = ["".join(verticalLine) for verticalLine in verticalLines]

    # Diagonals
    x = len(lines[0])
    y = len(lines)-1
    ## Bottoms left to top right
    diagonalsBL2TR = ["".join(BL2TR(lines, i)) for i in range(-y, x)]
    ## Top right to bottom left
    diagonalsTR2BL = ["".join(TR2BL(lines, i)) for i in range(x+y)]

    lines += verticalLines
    lines += diagonalsBL2TR
    lines += diagonalsTR2BL

    total = 0
    for line in lines:
        xmas = re.findall("XMAS", line)
        samx = re.findall("SAMX", line)
        total += len(xmas) + len(samx)

    print(total)

def BL2TR(mat, offset):
    return [ row[i+offset] for i,row in enumerate(mat) if 0 <= i+offset < len(row)]

def TR2BL(mat, offset):
    return [ row[-i+offset] for i,row in enumerate(mat) if 0 <= -i+offset <len(row) ]

solve()