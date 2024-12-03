import re
from operator import mul
from functools import reduce

def getLines(file):
    with open(file) as file:
        lines = [line.rstrip() for line in file]
    return lines

def solve():
    lines = "".join(getLines("./input.txt"))
    # Find all mul
    x = re.findall("mul\\([0-9]{1,3},[0-9]{1,3}\\)", lines)
    # Get only numbers e.g: [['2', '4'], ['5', '5'], ['11', '8'], ['8', '5']]
    x = [re.findall("[0-9]{1,3}", digits) for digits in x]
    # Convert to int : [[2, 4], [5, 5], [11, 8], [8, 5]]
    x = [[int(digit) for digit in digits] for digits in x]
    # Sum all multiplications
    x = sum(reduce(mul, digits) for digits in x)
    print(x)

solve()