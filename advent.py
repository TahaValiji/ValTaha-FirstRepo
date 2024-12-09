file = open("input.csv","r")
lines = file.read()
    
t=""
j=0

for i in range(len(lines)):
    if i%2 == 0:
        t += str(j) * int(lines[i])
        j+=1
    elif i%2 != 0:
        t += "." * int(lines[i])
        
s = t[::-1]
n = len(t)
c = t.count(".")

for a in range(n):
    
    if s[a] != ".":   
        b = t.find(".")
        t = t[:b] + s[a] + t[b+1:]
        t = t[:n-a-1] + "." + t[n-a:]
        
        if t[-c:] == c*'.':
            break
        
file1 = open('output.csv','w')
file1.write(t)
        
x = 0
for i in range(n-c):
    x += i * int(t[i])
    
print(x)
file.close()