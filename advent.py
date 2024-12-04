# To check XMAS horizontally(backwards), vertically(backwards), diagonally. 

total = 0
with open("input2.txt", 'r') as file:
    lines = file.readlines()
    
    for i in range(len(lines)):
        
        for j in range(len(lines[i])):
            
            # To check horizontal normal and backwards.
            if j < len(lines[i])-4:
                if lines[i][j:j+4] == ("XMAS" or "SAMX"):
                    total += 1
            
            # To check vertical normal and backwards.
            if i < len(lines)-4:     
                if lines[i:i+4][j] == ("XMAS" or "SAMX"):
                    total += 1
                
            # To check Diagonal.
            
print(total)