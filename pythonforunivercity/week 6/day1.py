'''w = int(input('Input number of words: '))
word = []
countchap = {}
for i in range(w):
    word.append(input(('')))
for i in range(w):
    countchap.setdefault(word[i][0], 0)
    countchap[word[i][0]] = countchap[word[i][0]] + 1
max = 0
key = ''
for i in countchap.keys():
    if countchap[i] >max:
        max = countchap[i]
        key = i
worduse = []
for i in word:
    if key in i[0]:
        worduse.append(i)
print(f'The popular character is {key}.')
print(f'The character is used in {len(worduse)} words.')
for i in worduse:
    print(i)'''
#5
'''
A = [[1,2,3],[4,5,6],[7,8,9]]
c = 2
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
def power_matrix(A,c) :
    Ac = A
    for i in range(c-1):
        Ac = mul_matrix(Ac,A)
    return Ac
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[0])):
      print(f'{A[i][j]:^6}', end = ' ')
    print()
ans = power_matrix(A,c)
print_matrix(ans)
'''
#2
'''dic = {'arm' : {'1':'n','2':'แขน'},'hello' : {'1':'v','2':'สวัสดี'}
       ,'beautiful' : {'1':'adj','2':'สวย'},'toilet' : {'1':'n','2':'ห้องน้ำ'},
       'kick' : {'1':'v','2':'เตะ'},'handsome' : {'1':'adj','2':'หล่อ'}}
while True:
    w = input()
    if w == '0':
        break
    if w not in dic.keys():
        print('Word not in dictionary.')
        continue
    n = input()
    while True:
        if n not in dic[w].keys():
            print('Invalid option.')
            n = input()
            continue
        break
    if w == '0':
        break
    print(dic[w][n])'''
#4
'''stdidy = {}
while True:
    stdid = int(input('Student ID : '))
    if stdid == 0:
        break
    y = int(input('years : '))
    stdidy[stdid] = y
sepa = int(input('Separate year: '))
for i in stdidy.keys():
    if stdidy[i] >= sepa:
        print(i)'''
#4
'''nDay = int(input('N = '))
mc = int(input('M = '))
cost = []
costmd = []
for i in range(nDay):
    cost.append(int(input(f'cost of day {i+1} = ')))
for i  in range(nDay-mc+1):
    add = 0
    for j in range(i,i+mc) :
        add += cost[j]
    costmd.append(add)
minc = costmd[0]
for i in costmd:
    if i < minc:
        minc= i
print(f'Min cost of {mc} days = {minc}')'''
#6
'''def creat_matrix():
    m = []
    for i in range(3):
        m.append([int(j) for j in input(f'Row {i+1} : ').split()])
    return m
def det_matrix(m):
    det = m[0][0]*(m[1][1]*m[2][2]-(m[2][1]*m[1][2]))\
          -m[0][1]*(m[1][0]*m[2][2]-(m[2][0]*m[1][2]))\
          +m[0][2]*(m[1][0]*m[2][1]-(m[2][0]*m[1][1]))
    return det
print(det_matrix(creat_matrix()))'''
#11
#12
'''t = input('Text: ')
s = input('Substring: ')
if s in t:
    sp = t.split(s)
    x = ''
    for i in range(len(sp)):
        if i != len(sp)-1:
            x += sp[i]+f'[{s}]'
        elif sp[-1] != '':
            x += sp[-1]
    print(x)
else :
    print('Not found')'''
#13
'''dna = input('DNA: ')
dtor = {'A': 'U','C':'G','G':'C','T':'A'}
rna = ''
for i in range(len(dna)):
    rna += dtor[dna[i]]
for i in range(len(rna)):
    if rna[i:i+3] == 'AUG':
        ami = 0
        break
for j in range(i,len(rna),3):
    if rna[j:j+3] in ['UAA','UGA','UAG']:
        break
    ami += 1
print(f'{ami} Amino acid(s)')'''
#14
'''def add_flight():
    f = input('Add data : ').split(' ')
    flight[f[0]] = {'start':f[1],'end':f[3],'np' :f[4],'fp' : f[6]}
def flightDataByCode():
    code = input('Enter code : ')
    print(f'{code} is from {flight[code]["start"]} '
          f'to {flight[code]["end"]}, '
          f'number of people booking is {flight[code]["np"]}/{flight[code]["fp"]}')
def showAllFlight():
    print('All flight data')
    for code in flight.keys():
        print(f'{code} is from {flight[code]["start"]} '
              f'to {flight[code]["end"]}, '
              f'number of people booking is {flight[code]["np"]}/{flight[code]["fp"]}')
def flight_booking():
    name = input('Enter your name : ')
    code = input('Enter flight code : ')
    if int(flight[code]['np']) < int(flight[code]['fp']):
        if name not in fb.keys():
            fb[name] = [code]
        elif name in fb.keys():
            fb[name].append(code)
        flight[code]['np'] = str(int(flight[code]['np']) + 1)
        print('Success')
    else :
        print('The flight is full, Sorry')
def show_people_flight_data():
    name = input('Enter your name : ')
    print(f'{name} is booking flight code =',end='')
    for i in fb[name]:
        print(' '+i,end ='')
    print()
print(''''''Select menu :
1. add flight data
2. flight data by code
3. show all flight data
4. flight booking
5. show people flight data
6. exit''''''')
flight = {}
fb = {}
while True:
    menu = int(input('menu : '))
    if menu == 6:
        print('EXIT!!!!!!!!!!!!!!!')
        break
    elif menu == 1:
        add_flight()
    elif menu == 2:
        flightDataByCode()
    elif menu == 3:
        showAllFlight()
    elif menu == 4:
        flight_booking()
    elif menu == 5:
        show_people_flight_data()
'''
#11
def transpose_matrix(A):
    tA= []
    for j in range(len(A[0])):
        add =[]
        for i in range(len(A)):
            add.append(A[i][j])
        tA.append(add)
    return tA
def plus_matrix(A,B) :
    sumAB = []
    for x in range(len(A)):
        add = []
        for y in range(len(A[0])):
            add.append(A[x][y] + B[x][y])
        sumAB.append(add)
    return sumAB
def minus_matrix(A,B):
    miAB = []
    for x in range(len(A)):
        add = []
        for y in range(len(A[0])):
            add.append(A[x][y] - B[x][y])
        miAB.append(add)
    return miAB
def mul_matrix(A,B) :
    mulAB = []
    for x in range(len(A)):
        add = []
        for z in range(len(B[0])):
            msum = 0
            for y in range(len(A[0])):
                msum += A[x][y] * B[y][z]
            add.append(msum)
        mulAB.append(add)
    return mulAB
def power_matrix(A,c):
    Ac = A
    for i in range(c - 1):
        Ac = mul_matrix(Ac, A)
    return Ac
def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:^6}', end=' ')
        print()
A = [[1, 2],
     [3, 4],
     [5, 6]]
B = [[7, 9, 11],
     [8, 10, 12]]
C = [[13, 14],
     [15, 16]]
D = [[100, 50],
    [20, 70]]
c = 2
total = mul_matrix(plus_matrix(A,transpose_matrix(B))
                   ,minus_matrix(power_matrix(C,c),D))
print_matrix(total)