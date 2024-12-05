# To check XMAS horizontally(backwards), vertically(backwards), diagonally. 

total = 0
with open("input2.txt", 'r') as file:
    lines = file.readlines()
    
    for i in range(len(lines)):
        for j in range(len(lines[i])-4):
            t=""
            for k in range(4):
                t += lines[i][j+k]
            
            if (t == "XMAS") or (t == "SAMX"):
                total += 1
                
    for i in range(len(lines)-4):
        for j in range(len(lines[i])):
            t=""
            for k in range(4):
                t += lines[i+k][j]
            
            if (t == "XMAS") or (t == "SAMX"):
                total += 1
                
    for i in range(len(lines)-3):
        for j in range(len(lines[i])-4):
            t=""
            for k in range(4):
                t += lines[i+k-1][j+k]
                      
            if (t == "XMAS") or (t == "SAMX"):
                total += 1
            
            t=""
            for k in range(4):
                t += lines[i+3-k][j+k]
                
            if (t == "XMAS") or (t == "SAMX"):
                total += 1
    
print(total)