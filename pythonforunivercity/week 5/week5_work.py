#1
'''def plus_matrix(A,B):
    sumAB = []
    for x in range(len(A)):
        add = []
        for y in range(len(A[0])):
            add.append(A[x][y]+B[x][y])
        sumAB.append(add)
    return sumAB
def  print_matrix(A):
    for x in range(len(A)):
        for y in range(len(A[0])):
            print(f'{A[x][y]:^6}',end =' ')
        print()
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]
print_matrix(plus_matrix(A,B))
'''
'''def minus_matrix(A,B):
    minusAB = []
    for x in range(len(A)):
        add = []
        for y in range(len(A[0])):
            add.append(A[x][y] - B[x][y])
        minusAB.append(add)
    return minusAB
def  print_matrix(A):
    for x in range(len(A)):
        for y in range(len(A[0])):
            print(f'{A[x][y]:^6}',end =' ')
        print()
print_matrix(minus_matrix(A,B))'''
'''def mul_const(A,c):
    constAB = []
    for x in range(len(A)):
        add = []
        for y in range(len(A[0])):
            add.append(c*A[x][y])
        constAB.append(add)
    return constAB
def  print_matrix(A):
    for x in range(len(A)):
        for y in range(len(A[0])):
            print(f'{A[x][y]:^6}',end =' ')
        print()
print_matrix(mul_const(A,c))'''
#4
'''n = int(input('Number of inputs: '))
call = {}
for i in range(n):
    name,num = input().split()
    call[name] = int(num)
while True:
    s = input('student: ')
    if s == '' :
        print('End')
        break
    print(f'{s}\'s score is {call[s]}')'''
#5
'''n = int(input('How many animals are there in the zoo? : '))
call = {}
for i in range(n):
    animal,food = input().split()
    call[animal] = food
ask = int(input('How many questions do you want to ask? : '))
for i in range(ask):
    s = input()
    if s not in call.keys() :
        print('Sorry we don\'t have that animal.')
    else:
        print(call[s])'''
'''
n = int(input('Number of inputs: '))
nscore = {}
for i in range(n):
    if i == 0:
        name = input('Input name: ')
        score = float(input('Input score: '))
        nscore[name] = [score]
        continue
    name = input('Input name: ')
    score = float(input('Input score: '))
    if name in nscore.keys():
        nscore[name].append(score)
    else :
        nscore[name] = [score]
for i in nscore.keys():
    sum = 0
    for y in range(len(nscore[i])):
        sum += nscore[i][y]
    nscore[i] = sum/len(nscore[i])
max = 0
for i in nscore.keys():
    if nscore[i] > max:
        max = nscore[i]
        nmax = i
print(f'Top score is {nmax}: {max:.2f}')
'''
#l01
'''n = int(input())
for x in range(n):
    for y in range(n):
        if x==0 or y==0 or x==y or x==(n-1-y) or y ==(n-1) or x == (n-1):
            print('.',end='')
        else :
            print(' ',end ='')
    print()'''
#l02
'''A = [[1,2],[3,4],[5,6]]
B = [[7,9,11],[8,10,12]]
C = [[13,14],[15,16]]
c = 2
def transpose_matrix(A):
    tA = []
    for x in range(len(A[0])):
        add = []
        for y in range(len(A)):
            add.append(A[y][x])
        tA.append(add)
    return tA
def print_matrix(A):
    for y in range(len(A)):
        for x in range(len(A[0])):
            print(f'{A[y][x]:^6}', end=' ')
        print()
print_matrix(transpose_matrix(A))'''
#lo3
'''A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
B = [[22,13,23],
     [54,43,21],
     [23,78,71]]
def mul_matrix(A,B):
    mulAB = []
    for x in range(len(A)):
        add = []
        for z in range(len(B[0])):
            msum = 0
            for y in range(len(A[0])):
                msum += A[x][y]*B[y][z]
            add.append(msum)
        mulAB.append(add)
    return mulAB
def  print_matrix(A):
    for x in range(len(A)):
        for y in range(len(A[0])):
            print(f'{A[x][y]:^6}',end =' ')
        print()
print_matrix(mul_matrix(A,B))'''
#l04
'''def creatgrid(x,y):
    grid = []
    for i in range(y+2):
        add = []
        for j in range(x+2):
            add.append('0')
        grid.append(add)
    return grid
def print_matrix(A):
    for x in range(1,len(A)-1):
        for y in range(1,len(A[0])-1):
            print(A[x][y], end=' ')
        print()
x,y = map(int,input('Grid Size: ').split())
grid = creatgrid(x,y)
n = int(input('Number of mine(s): '))
for i in range(n):
    x,y = map(int,input(f'Mine#{i+1}: ').split())
    grid[y+1][x+1] = 'X'
for x in range(1,len(grid)-1):
    for y in range(1,len(grid[0])-1):
        if grid[x][y] == 'X':
            continue
        sum = 0
        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                if i == x and j ==y:
                    continue
                elif grid[i][j] == 'X':
                    sum += 1
        grid[x][y] = str(sum)
print_matrix(grid)'''
#l05
'''num = [int(i) for i in input().split()]
while True:
    x,y = map(int,input().split())
    if x<0 :
        x = x+len(num)
    if y<0 :
        y = y+len(num)
    if (x<0 and y >= len(num)) or (y<0 and x >= len(num)):
        print('x and y Bad Input')
        continue
    elif x<0 :
        print('x Bad Input')
        continue
    elif y>= len(num) :
        print('y Bad Input')
        continue
    elif x>y:
        break
    sum = 0
    for i in range(x,y+1):
        sum += num[i]
    print(sum)'''
'''def mul_matrix(A,B):
  mul_mat = []
  for i in range(len(A)):
    tmp = []
    for j in range(len(B[0])):
      mysum = 0
      for k in range(len(A[0])):
        mysum += A[i][j] * B[j][k]
      tmp.append(mysum)
    mul_mat.append(tmp)
  return mul_mat

def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[0])):
      print(f'{A[i][j]:^6}', end = ' ')
    print()

# main program #
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]
c = mul_matrix(A,B)
print_matrix(c)'''
'''def mul_matrix(A,B):
  mul_mat = []
  mysum = 0
  for i in range(len(A)):
    tmp = []
    for j in range(len(A[0])):
      num_mul = A[i][j]*B[j][i]
      tmp.append(num_mul)
      for k in range(len(tmp)):
        mysum += tmp[k]
    mul_mat.append(mysum)
  return mul_mat

def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[0])):
      print(f'{A[i][j]:^6}', end = ' ')
    print()

# main program #
A = [[1,2,3],[4,5,6],[7,8,9]]
B = [[22,13,23],[54,43,21],[23,78,71]]
C = mul_matrix(A,B)
print(C)'''

'''x = '00x541d aaaa -> bbbb 0 / 50'
print(x.split())'''
print(20//3)













