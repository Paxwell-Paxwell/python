def creat(n):
    cgrid =[]
    for i in range(n+1):
        add = []
        for j in range(n+1):
            if i == 0:
                if j == 0:
                    add.append(' ')
                elif j != 0 :
                    add.append(j)
            elif j == 0 :
                 add.append(i)
            else :
                 add.append('*')
        cgrid.append(add)
    return cgrid
def ty1() :
    ty1= creat(n)
    k=0
    for i in range(1,len(ty1)):
        for j in range(1,len(ty1[0])):
            if k < len(w):
                ty1[i][j] = w[k]
                k += 1
    return ty1
def ty3() :
    ty2= creat(n)
    k=0
    for i in range(len(ty2)-1,0,-1):
        for j in range(len(ty2[0])-1,0,-1):
            if k < len(w):
                ty2[i][j] = w[k]
                k += 1
    return ty2
def ty2() :
    ty2= creat(n)
    k=0
    for i in range(1,len(ty2)):
        for j in range(1,len(ty2[0])):
            if k < len(w):
                ty2[j][i] = w[k]
                k += 1
    return ty2
def ty4() :
    ty4= creat(n)
    k=0
    for i in range(len(ty4)-1,0,-1):
        for j in range(len(ty4[0])-1,0,-1):
            if k < len(w):
                ty4[j][i] = w[k]
                k += 1
    return ty4
def ty5() :
    ty5= creat(n)
    k=0
    for i in range(1,len(ty5)):
        for j in range(1,len(ty5[0])):
            if k < len(w):
                ty5[j][i] = w[k]
                k += 1
    return ty5
def print_grid(grid) :
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j],end = ' ')
        print('')


print('Enter a sentence or pharse and then press ENTER')
w = input('')
n = 0
while True:
    if n ** 2 >= len(w):
        break
    n += 1
ch = int(input('Enter output type (only 1..5:) '))
if ch == 1 :
    grid = ty1()
elif ch == 2 :
    grid = ty2()
elif ch == 3 :
    grid = ty3()
elif ch == 4 :
    grid = ty4()
elif ch == 5 :
    grid = ty5()
print_grid(grid)
