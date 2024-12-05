def getLines(file):
    with open(file) as file:
        lines = [line.rstrip() for line in file]
    return lines

def solve():
    lines = getLines("./input.txt")
    sectionsSplit = lines.index("")
    # Page Ordering Rules ->['47|2', '45|4'] [['47','2'], ['45','4']] -> [[47,2], [45,4]]
    por = [x for x in lines[:sectionsSplit]]
    # Page number of each update -> [['1,2'],['3,4']] -> [['1','2'],['3','4']] -> [[1,2],[3,4]]
    pnu = [[int(x) for x in y] for y in [x.split(",") for x in lines[sectionsSplit+1:]]]
    ####
    incorrects = []
    solutions = []
    for update in pnu:
        correct = True
        solutions.append([])
        for i in range(len(update)):
            befores = [f"{update[i]}|{update[j+1]}" for j in range(i, len(update)-1)]
            forbidden = [f"{update[j+1]}|{update[i]}" for j in range(i, len(update)-1)]
            afters = [f"{update[j]}|{update[i]}" for j in range(0,i)]
            correct = correct and (all(i in por for i in befores) and all(i in por for i in afters))
            for forb in forbidden:
                if forb in por:
                    solutions[-1].append(forb)
                    correct = False
                    break
        if not correct:
            incorrects.append(update)
    
    # sulutions[i] contains solutions of incorrects[i]
    solutions = [x for x in solutions if x != []]
    temps = []
    for solution in solutions:
        s = []
        for x in solution:
            t = x.split("|")
            s.append([int(t[0]), int(t[1])])
        temps.append(s)
    solutions = temps
    for i in range(len(solutions)):
        print(incorrects[i])
        for sol in solutions[i]:
            incorrects[i] = invert(incorrects[i], sol[0], sol[1])
            print(f">> {incorrects[i]}")

    print(solutions)

def invert(list, x, y):
    indexX = list.index(x)
    indexY = list.index(y)
    list[indexX], list[indexY] = list[indexY], list[indexX]
    return list

solve()