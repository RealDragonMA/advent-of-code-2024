import re

def getLines(file):
    with open(file) as file:
        lines = [line.rstrip() for line in file]
    return lines

def solve():
    lines = getLines("./input.txt")

    # Len of a line (all the same)
    lineLength = len(lines[0])
    # Number of lines
    lineHeight = len(lines)
    
    # Divide all by a 3x3 matrix with just diagonals value
    allMat3x3 = []
    for i in range(0, lineHeight-2):
        for j in range(0, lineLength-2):
            allMat3x3.append([
                lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2],
                lines[i][j+2] + lines[i+1][j+1] + lines[i+2][j]
            ])
        
    total = 0
    for mat in allMat3x3:
        if (mat[0] == 'SAM' or mat[0] == 'MAS') and (mat[1] == 'SAM' or mat[1] == 'MAS'):
            total+=1
            
    print(total)

    


def BL2TR(mat, offset):
    return [ row[i+offset] for i,row in enumerate(mat) if 0 <= i+offset < len(row)]

def TR2BL(mat, offset):
    return [ row[-i+offset] for i,row in enumerate(mat) if 0 <= -i+offset <len(row) ]

solve()