# Directions:
# > Right
# < Left
# ^ up
# v down

Directions = {
    "^": "up",
    ">": "Right",
    "v": "down",
    "<": "Left"
}

def findGuard(lines: list[str]):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] in Directions:
                return i,j
            
def up(n: int,m: int,lines: list[str],flag: bool = True):
    steps = 0
    steps2 = 0
    # n -> at which number of line guard is located.
    # dir -> direction of guard.
    # m -> position of that guard at that line n.
    for i in range(n-1, -1, -1):
        if lines[i][m] == ".":
            steps += 1
            lines[i] = lines[i][:m] + "X" + lines[i][m+1:]
        elif lines[i][m] == "X":
            steps+=1
            steps2+=1
        elif lines[i][m] == "#":
            break
    else:
        if lines[0][m] == ".":
            flag = False
    n -= steps
    return n,steps,flag,steps2

def right(n:int ,m: int,lines: list[str],flag: bool = True):
    # n -> at which number of line guard is located.
    # dir -> direction of guard.
    # m -> position of that guard at that line n.
    steps = 0
    steps2 = 0
    for i in range(m+1,len(lines[n])):
        if lines[n][i] == ".":
            steps += 1
            lines[n] = lines[n][:i] + "X" + lines[n][i+1:]
        elif lines[n][i] == "X":
            steps+=1
            steps2+=1
        elif lines[n][i] == "#":
            break
    else:
        if lines[n][len(lines[n])-1] == ".":
            flag = False
    m += steps
    return m,steps,flag,steps2

def down(n:int ,m: int,lines: list[str],flag: bool = True):
    steps = 0
    steps2 = 0
    # n -> at which number of line guard is located.
    # dir -> direction of guard.
    # m -> position of that guard at that line n.
    for i in range(n+1,len(lines)):
        if lines[i][m] == ".":
            steps += 1
            lines[i] = lines[i][:m] + "X" + lines[i][m+1:]
        elif lines[i][m] == "X":
            steps+=1
            steps2+=1
        elif lines[i][m] == "#":
            break
    else:
        if lines[len(lines)-1][m] == ".":
            flag = False
    n += steps
    return n,steps,flag,steps2

def left(n:int ,m: int,lines: list[str],flag: bool = True):
    # n -> at which number of line guard is located.
    # dir -> direction of guard.
    # m -> position of that guard at that line n.
    # n -> at which number of line guard is located.
    # dir -> direction of guard.
    # m -> position of that guard at that line n.
    steps = 0
    steps2 = 0
    for i in range(m, -1, -1):
        if lines[n][i] == ".":
            steps += 1
            lines[n] = lines[n][:i] + "X" + lines[n][i+1:]
        elif lines[n][i] == "X":
            steps += 1
            steps2 += 1
        elif lines[n][i] == "#":
            break
    else:
        if lines[n][0] == ".":
            flag = False
    m -= steps
    return m,steps,flag,steps2

def main():
    STEPS = 0   # STEPS -> STEPS to reach obstacles and the end of the maze.
    STEPS2 = 0
    with open("input.txt") as file:
        lines = file.readlines()    
        n,m= findGuard(lines)    # type: ignore # n -> at which number of line guard is located, dir -> direction of guard.
        
        flag = True
        while flag:
            n,steps,flag,steps2 = up(n,m,lines)    # m -> position of that guard at that line n.
            STEPS += steps
            STEPS2+= steps2
            print(f"steps: {STEPS}")
            if flag is False:
                break
            
            m,steps,flag,steps2 = right(n,m,lines)
            STEPS += steps
            STEPS2+= steps2
            print(f"steps: {STEPS}")
            if flag is False:
                break
            
            n,steps,flag,steps2 = down(n,m,lines)
            STEPS += steps
            STEPS2+= steps2
            print(f"steps: {STEPS}")
            if flag is False:
                break
            
            m,steps,flag,steps2 = left(n,m,lines)
            STEPS += steps
            STEPS2+= steps2
            print(f"steps: {STEPS}")
            if flag is False:
                break
            
    print(STEPS-STEPS2)
        
if __name__ == "__main__":
    main()