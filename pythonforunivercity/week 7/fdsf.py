#1
'''f = {}
n = int(input(('N : ')))
for  i in range(n):
    fr,nu = input().split()
    f[fr] = int(nu)
plus = [str(i).strip() for i in input().split('+')]
t = 0
for i in plus:
    t += f[i]
print(t)'''
#2
'''def checkchain(i):
    nsame = 0
    for j in range(len(text[i])):
        if text[i][j] != text[i-1][j]:
            nsame += 1
    if nsame <= 2 :
        return True
    else :
        return False
text = input('Text: ').split()
chain  = {}
nc = 1
for i in range(len(text)):
    if i == 0:
        chain[nc] = [text[0]]
        continue
    if checkchain(i):
        chain[nc].append(text[i])
    else :
        nc += 1
        chain[nc] = [text[i]]
maxc = 0
for i in chain.values():
    if len(i) > maxc:
        maxc = len(i)
print(f'{len(chain)} Chain(s). Maximum length is {maxc} word(s).')'''
#3
'''def newarea(area):
    narea = []
    for i in range(len(area)+2):
        add = []
        for j in range(len(area[0])+2):
            add.append(0)
        narea.append(add)
    for i  in range(len(area)):
        for j in range(len(area[0])):
            narea[i+1][j+1] = area[i][j]
    return narea
def check():
    for i in range(len(area)-1):
        if len(area[i+1]) != len(area[i]):
            return True
area = []
price = []
while True:
    w = [int(i) for i in input().split()]
    if len(w) == 0:
        break
    area.append(w)
if check():
    print("Can't Buy")
else :
    narea = newarea(area)
    for i in range(1,len(narea)-2):
        for j in range(1,len(narea[0])-2):
            price.append(narea[i][j]+narea[i][j+1]*1.1+narea[i+1][j+1]*1.1+narea[i+1][j]*1.1**2)
    for i in range(len(narea)-2,1,-1):
        for j in range(1,len(narea[0])-2):
            price.append(narea[i][j]+narea[i][j+1]*1.1+narea[i-1][j+1]*1.1+narea[i-1][j]*1.1**2)
    min = price[0]
    for i in price:
        if min > i:
            min = i
    print(f'{min:.2f}')'''
#5
'''n = int(input())
sibling = {}
for i in range(n):
    a = input().split()
    x,link,z = a[0],a[2],a[-1]
    if link in ['mother','father']:
        if x not in sibling.keys():
            sibling[x] = [z]
        else :
            sibling[x].append(z)
ch = input('').split()
for i in sibling.keys():
    x = 'No'
    if ch[1] in sibling[i] and ch[3] in sibling[i]:
        x = 'Yes'
        break
print(x)'''
#3
'''a = int(input('a : '))
b = int(input('b : '))
x= a*b
if a > b:
    a,b = b,a
while True:
    if a > b:
        a, b = b, a
    b = b%a
    if b == 0:
        break
print(f'GCD : {a}')
print(f'LCM : {int(x/a)}')'''
#6
def building(r):
    bg = []
    for i in range(r):
        add= [int(i) for i in input().split()]
        bg.append(add)
    return bg
def nview():
    building_i_can_see = 0
    for j in range(len(build[0])):
        height = build[0][j]
        building_i_can_see += 1
        for i in range(1,len(build)):
            if height < build[i][j]:
                height = build[i][j]
                building_i_can_see += 1
    return building_i_can_see
def sview():
    building_i_can_see = 0
    for j in range(len(build[0])):
        height = build[r-1][j]
        building_i_can_see += 1
        for i in range(len(build)-2,-1,-1):
            if height < build[i][j]:
                height = build[i][j]
                building_i_can_see += 1
    return building_i_can_see
def eview():
    building_i_can_see = 0
    for i in range(len(build)):
        height = build[i][c-1]
        building_i_can_see += 1
        for j in range(len(build[0]) - 2, -1, -1):
            if height < build[i][j]:
                height = build[i][j]
                building_i_can_see += 1
    return building_i_can_see
def wview():
    building_i_can_see = 0
    for i in range(len(build)):
        height = build[i][0]
        building_i_can_see += 1
        for j in range(1, len(build[0])):
            if height < build[i][j]:
                height = build[i][j]
                building_i_can_see += 1
    return building_i_can_see
r,c = map(int,input('City Size: ').split())
build = building(r)
dataview = {'N': nview() ,'S':eview(),'E':eview(),'W':wview() }
rank = ['N','S','E','W']
for i in range(3):
    max = dataview[rank[i]]
    for j in range(i+1,4):
        if max < dataview[rank[j]]:
            rank[i],rank[j] =rank[j],rank[i]
print(rank[0],end=' ')
for i in range(1,len(rank)):
    if dataview[rank[i]] == dataview[rank[0]]:
        print(rank[i],end=' ')





 












