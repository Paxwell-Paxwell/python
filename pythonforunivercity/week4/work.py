#1
'''
N = 10
def Nplus(a):
    global N
    N = N+a
def Nminus(a):
    global N
    N = N - a
def Ntimes(a):
    global N
    N = N * a
def Ndivided(a):
    global N
    N = N/a
Nplus(5)
Nminus(3)
Ntimes(6)
Ndivided(3)
print(f'{N:.0f}')
c = input()
if c == '1':
    Nplus(12)
    print(f'{N:.0f}')
if c == '2':
    Nminus(6)
    print(f'{N:.0f}')
if c == '3':
    Ntimes(2)
    print(f'{N:.0}')
if c == '4':
    Ndivided(6)
    print(f'{N:.0f}')
'''
#2
import sys

'''N = int(input('N = '))
codl = []
for i in range(1,N+1):
    cod = int(input(f'cost of day {i} = '))
    codl.append(cod)
l3d = []
for i in range(len(codl)-2):
    sum = 0
    for y in range(0,3):
        sum += codl[i+y]
    l3d.append(sum)
min = l3d[0]
for i in range(len(l3d)):
    if min >= l3d[i] :
        min = l3d[i]
print(f'Min cost of 3 days = {min}')'''
#3
'''x,y = map(int,input('Grass : ').split(' '))
ar = [int(x) for x in input().split()]
r = 0
for i in range(len(ar)):
    if ar[i] > y:
        r += 1
print(r)'''
#4
import sys
'''n = int(input('N : '))
ar = [int(x) for x in input().split()]
for i in range(len(ar)) :
    x = 'yes'
    if ar[i] == 1 :
       for y in range(i,len(ar),2):
           if ar[y] == 2 :
               x = 'no'
               break
       for y in range(i+1,len(ar),2):
           if ar[y] == 1 :
               x = 'no'
               break
       break
    elif ar[i] == 2 :
        for y in range(i, len(ar), 2):
            if ar[y] == 1:
                x = 'no'
                break
        for y in range(i + 1, len(ar), 2):
            if ar[y] == 2:
                x = 'no'
                break
        break
print(x)'''
#5
'''pn = []
while True :
    num = int(input('Enter a positive number: '))
    if num > 0 :
        pn.append(num)
    if len(pn) == 5:
        break
sum = 0
for i in pn:
    sum += i
i=0
for i in range(len(pn)):
    for y in range(i,len(pn)):
        if pn[i]>=pn[y]:
            pn[i],pn[y] = pn[y],pn[i]
print(f'sum: {sum}')
print(f'min: {pn[0]}')
print(f'max: {pn[-1]}')
print(f'med: {pn[2]}')'''
#6
''''p = input('')
i = 0
while i < len(p) :
    d = input('')
    t = 'Succeed!!'
    if d != p[i] :
        t = 'Fail!!'
        break
    i +=1
print(t)
'''
#7
'''def draw(m):
    for i in range(len(m)):
        print(m[i]*(i+1))
while  True:
    m = [str(x) for x in input().split()]
    if m[0] == '0':
        print('Good Bye.')
        break
    draw(m)
'''
#21

'''a = list(input('Input name: '))
for i in range(len(a)):
    a[i] = a[i].upper()
    n = ''
    for j in a :
        n += j
    print(n)
    a[i] = a[i].lower()
'''
#22
'''a = list(input('Input name: '))
for i in range(len(a)):
    n = ''
    for j in range(len(a)):
        if a[j] == a[i]:
            a[j] = a[j].upper()
        n += a[j]
        a[j] = a[j].lower()
    print(n,end = ' ')
    n = ''
    for rj in range(len(a)-1,-1,-1):
        if a[rj] == a[len(a)-i-1]:
            a[rj] = a[rj].upper()
        n += a[rj]
        a[rj] = a[rj].lower()
    print(n)
    a[i] = a[i].lower()'''
#23
'''def ch(menu,x):
    if menu == 'A':
        A.append(x)
    elif menu == 'S' :
         print(A[x])
    elif menu == 'R' :
        A.remove(A[x])
    elif menu == 'E' and x == 0 :
        global on
        on = 0
A = list(map(int,input().split()))
while True:
    on = 1
    menu, x = input().split()
    x = int(x)
    ch(menu,x)
    if on == 0:
        for i in A:
            print(i,end =' ')
        break
'''
#24
'''def check(num1,num2):
    global luck
    if num1+num2 == '08':
        sum = int(n[1])
        for i in range(2,len(n)):
            sum += int(n[i])
        if sum%13 == 0 and sum < 56:
            luck = 'Have bad luck.'
    elif num1+num2 == '09':
        for i in range(2,len(n)-1):
            check =['20','13','18', '80' , '31' ,'93']
            if n[i]+n[i+1] in check :
                luck = 'Have bad luck.'
                break
n = list((input('')))
luck = 'Have good luck.'
check(n[0],n[1])
print(luck)
'''
#25
'''
lcn = input('Enter lucky number : ')
aoc = int(input('Enter amount of candidates : '))
id = []
lcninid =[]
for i in range(aoc):
    id.append(int(input(f'Enter ID card number {i+1}: ')))
for i in range(len(id)):
    for y in range(i,len(id)):
        if id[i]<=id[y]:
            id[i],id[y] = id[y],id[i]
for i in range(len(id)):
    luckyInid = list(str(id[i]))
    x = 0
    for j in range(len(luckyInid)):
        if  luckyInid[j] == lcn :
            x += 1
    lcninid.append(x)
max = lcninid[0]
j = 0
for i in range(len(lcninid)):
    if max < lcninid[i]:
        max = lcninid[i]
        j = i
print(f'Winner: {id[j]}')
'''
#26
'''
def checkprime():
    prime = True
    if num == 1:
       prime = False
    elif num == 2:
       prime  = True
    else :
        for i in range(2,num):
            if num%i == 0:
               prime = False
               break
    return prime
num = int(input(''))
prime_num = []
while num > 0 :
    prime = checkprime()
    if prime:
        prime_num.append(num)
    num = int(input(''))
l = 0
for i in prime_num:
    print(i,end = ' ')
    l += 1
    if l >= 10 :
        print('')
        l = 0
'''
#27
'''n = int(input('N: '))
m = int(input('M: '))
dm = []
for r in range(n):
    if r == 0:
        num = int(input(f'Input number {r+1}: '))
        x = num%m
        dm.append(x)
    else :
        num = int(input(f'Input number {r+1}: '))
        x = num%m
        if x not in dm:
            dm.append(x)
print(len(dm))'''
#28
'''def checkprime():
    prime = True
    if num == 1:
       prime = False
    elif num == 2:
       prime  = True
    else :
        for i in range(2,num):
            if num%i == 0:
               prime = False
               break
    return prime
n = int(input('N: '))
prime_num = []
num = n
while True:
    prime = checkprime()
    if prime:
        prime_num.append(num)
    num += 1
    if len(prime_num)>=2:
        if prime_num[-1]-prime_num[-2] == 2:
            print(f'({prime_num[-2]}, {prime_num[-1]})')
            break'''
#29
'''def commaCode(ml):
    x =''
    for i in ml:
        if i == ml[-1] and len(ml) == 1:
            x += i
        elif i == ml[-1] and len(ml) > 1:
            x += f'and {ml[-1]}'
        else:
             x += f'{i}, '
    return x

ml = list(input('Input: ').split())
print(commaCode(ml))'''
#210
'''def rotate_right(grid):
    rgrid =[]
    for y in range(len(grid[0])):
        grid1d = []
        for x in range(len(grid)-1,-1,-1):
            grid1d.append(grid[x][y])
        rgrid.append(grid1d)
    return rgrid
def rotate_left(grid):
    rgrid = []
    for y in range(len(grid[0])-1,-1,-1):
        grid1d = []
        for x in range(len(grid)):
            grid1d.append(grid[x][y])
        rgrid.append(grid1d)
    return rgrid
def print_grid(grid):
    for x in range(len(grid)):
        st =''
        for y in range(len(grid[0])):
            st += grid[x][y]
        print(st)
grid1 = [['.','.','.','.','.','.'],
        ['.','o','o','.','.','.'],
        ['o','o','o','o','.','.'],
        ['o','o','o','o','o','.'],
        ['.','o','o','o','o','o'],
        ['o','o','o','o','o','.'],
        ['o','o','o','o','.','.'],
        ['.','o','o','.','.','.'],
        ['.','.','.','.','.','.']]
grid2 = [['.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.'],
        ['.','.','.','.','o','.','o'],
        ['o','o','.','o','.','o','.'],
        ['o','o','o','o','o','.','.'],
        ['o','o','.','o','.','o','.'],
        ['.','.','.','.','o','.','o'],
        ['.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.']]
grid = rotate_left(rotate_left(grid1))
print_grid(grid)
'''
'''num_id = []
times_max = 0
num_max = 0

lucky_num = input('Enter lucky number : ')
num_candidate = int(input('Enter amount of candidates : '))

for i in range(num_candidate):
  id_num = input(f'Enter ID card number {i+1}: ') #id_num is str.
  num_id.append(id_num)
for i in range(len(num_id)):
    for y in range(i,len(num_id)):
        if num_id[i]<=num_id[y]:
            num_id[i],num_id[y] = num_id[y],num_id[i]
longnum = len(num_id[0])
for i in range(len(num_id)):
  times = 0
  for j in range(longnum):
    if num_id[i][j] == lucky_num:
      times += 1
  if times_max<times :
      times_max = times
      num_max = num_id[i]
print(f'Winner: {num_max}')
'''
a = 5
print(a)

