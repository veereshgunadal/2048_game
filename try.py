def movement():
    l = [0,2,0,2]
    l1= [0,0,0,0]
    
    j = 0
    for i in range(4):
        flag = False
        if l[i] != 0:
            l1[j] = l[i]
            flag = True
            
        if flag == True:
            j = j+1

def merge():
    l = [2,2,0,2]
    l1 = [0,0,0,0]
    
    for i in range(3):
        if l[i] == l[i+1]:
            l1[i] = l[i] + l[i+1]
            l[i+1] = 0

l = []
for i in range(4):
    l.append([0]*4)

l[1][0] = 1
l[2][0] = 2
l1 = []
for i in range(4):
    l1.append([0]*4)

for i in range(4):
    for j in range(4):
        l1[j][i] = l[i][j]
for i in range(4):
    print(l1[i])
