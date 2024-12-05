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
    corrects = []
    for update in pnu:
        correct = True
        for i in range(len(update)):
            befores = [f"{update[i]}|{update[j+1]}" for j in range(i, len(update)-1)]
            forbidden = [f"{update[j+1]}|{update[i]}" for j in range(i, len(update)-1)]
            afters = [f"{update[j]}|{update[i]}" for j in range(0,i)]
            correct = correct and (all(i in por for i in befores) and all(i in por for i in afters))
            for forb in forbidden:
                if forb in por:
                    correct = False
                    break
        if correct:
            corrects.append(update)
    
    mids = sum(correct[len(correct)//2] for correct in corrects)
    print(mids)
        
               
    


solve()