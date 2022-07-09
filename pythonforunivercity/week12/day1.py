'''def create_zero_matrix(m, n):
    return[[0 for j in range(n)] for i in range(m)]


print(create_zero_matrix(2, 3))
print(create_zero_matrix(7, 5))
print(create_zero_matrix(10, 10))'''
'''def plus(A,B):
   return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A)) ]
print(plus([[1,2],[3,4]],[[5,6],[7,8]]))
print(plus([[1,2],[3,4],[5,6]],[[7,8],[9,10],[11,12]]))
print(plus([[1,2,3,4,5],[3,4,6,7,8],[5,6,9,10,11]],[[12,23,34,45,56],[32,43,46,57,78],[51,63,59,80,71]]))'''


'''def transpose(A):
    return [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]
print(transpose([[1,2],[3,4]]))
print(transpose([[1,2],[3,4],[5,6]]))
print(transpose([[1,2,3,4,5],[3,4,6,7,8],[5,6,9,10,11]]))'''
'''def multiply(A,B):
    return[[sum([A[i][k]*B[k][j] for k in range(len(A[0]))]) for j in range(len(B[0]))] for i in range(len(A)) ]
print(multiply([[1,2],[3,4]],[[5,6],[7,8]]))
print(multiply([[1,2],[3,4],[5,6]],[[7,8],[9,10]]))
print(multiply([[1,2,3,4,5],[3,4,6,7,8],[5,6,9,10,11]],[[12,23,34,45,56,44],[32,43,46,57,78,33],[51,63,59,80,71,22],[1,2,3,4,5,34],[6,7,8,9,10,99]]))'''
'''class Country:
  nbCountry = 0
  def __init__(self, country, population, EU,coastline):
    self.country = country
    self.population = float(population)
    self.EU = EU
    self.coastline = coastline
    Country.nbCountry += 1
def readCountry():
  myCountry = []
  filename = input('Enter File name: ')
  with open(filename) as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      country,population,EU,coastline = cc[0], cc[1], cc[2], cc[3]
      myCountry.append(Country(country,population,EU,coastline))
  return myCountry
myCountry = readCountry()
con = {}
for i in myCountry:
    if i.EU == 'no' and i.coastline == 'yes':
        con[i.country] = i.population
for k,v in con.items():
    print(k,v)'''
'''
class City:
  nbCity = 0
  def __init__(self, city, country, latitude, longitude, temperature):
    self.city = city
    self.country = country
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.temperature = float(temperature)
    City.nbCity += 1
def readCity():
  myCity = []
  filename = input('Enter file name: ')
  with open(filename) as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      city,country,lat,long,temp = cc[0],cc[1],float(cc[2]),float(cc[3]),float(cc[4])
      myCity.append(City(city,country,lat,long,temp))
  return myCity
mycity = readCity()
min = 999999
max = -999999
summ = 0
for i in mycity:
    summ += i.temperature
    if max < i.temperature:
        max = i.temperature
    if min > i.temperature:
        min = i.temperature
aver = summ / City.nbCity
print(f'Minimum: {min:.2f}')
print(f'Maximum: {max:.2f}')
print(f'Average temperature: {aver:.4f}')'''
'''
def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return f(n-1)+f(n-2)+f(n-3)
num = int(input('n: '))
print(f(num),end='')'''
'''def minus(a,b):
    return sorted([int(i) for i in list(set(a)-set(b))])
A = input('Input set A: ').split()
B = input('Input set B: ').split()
if A != B:
    print(f'A minus B: {minus(A,B)}')
else:
    print(f'A minus B: empty set')'''
'''def union(a,b):
    return sorted([int(i) for i in list(set(a).union(set(b)))])
A = input('Input set A: ').split()
B = input('Input set B: ').split()
print(f'A union B: {union(A,B)}')'''
'''
def creat(n):
    matrix = []
    for i in range(n):
        add = []
        for j in range(n):
            add.append(0)
        matrix.append(add)
    return matrix
def count(matrix):
    x,y = len(matrix)-1,0
    num = 1
    for i in range(1,n+1):
        for j in range(i):
            if i%2==0:
                matrix[x][y] = num
                if j != i-1:
                    x += 1; y += 1
                num +=1
            else :
                matrix[x][y] = num
                if j != i - 1:
                    x -= 1; y -= 1
                num += 1
        if y ==0:
            if x != 0:
                x -=1
        else :
            if y != len(matrix)-1:
                y += 1
    if y == 0:
        y += 1
    else:
        x -= 1
    for i in range(len(matrix)-1,0,-1):
        for j in range(i):
            if i % 2 == 0:
                matrix[x][y] = num
                if j != i - 1:
                    x += 1
                    y += 1
                num += 1
            else:
                matrix[x][y] = num
                if j != i - 1:
                    x -= 1
                    y -= 1
                num += 1
        if x == 0:
            if y != len(matrix) - 1:
                y += 1
        else:
            if x != 0:
                x -= 1

def print_matrix(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            print(f'{matrix[x][y]:3.0f}', end=' ')
        print()
n = int(input())
matrix = creat(n)
count(matrix)
print_matrix(matrix)
'''
'''
def hash(a,b):
    if ord(a)>=ord(b):
        return ord(b)+10
    elif ord(a)<ord(b):
        return ord(a)-7
def isPhotobook(strr):
    global x
    if 65<=ord(strr[0].upper())<=90 and 65<=ord(strr[-1].upper())<=90:
        x = True
    else:
        x = False
    return x
def calKey(strr,key = 0):
    for i in range(0,len(strr)-1):
        key += hash(strr[i],strr[i+1])
    return key
def isPhotobookGenuine(key):
    if not x :
        return "Incorrect Type"
    elif key%2 == 0:
        return True
    else :
        return False
def isAlbumGenuine(key):
    if x:
        return "Incorrect Type"
    elif key % 2 == 0:
        return False
    else:
        return True

def solve():
    n = int(input())
    ph = 0
    al = 0
    for i in range(n):
        code = input()
        key = calKey(code)
        if isPhotobook(code):
            if isPhotobookGenuine(key):
                ph += 1
        else:
            if isAlbumGenuine(key):
                al += 1
    print(ph)
    print(al)
solve()
'''
'''
def f(n,x=0):
    so = sorted([a,b,c])
    if n == 0:
        return 1
    if n < 0:
        return 0
    for i in so:
        if n >= i :
            x += f(n-i)
    return x
n = int(input('n : '))
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
print(f(n))'''
'''class cow:
    def __init__(self,name,weight):
        self.name = name; self.weight = weight
    def __lt__(self, other):
        return self.weight < other.weight
def base10to2(num):
    if num == 0:
        return [0]
    digits = []
    while num:
        a = num % 2
        digits.append(a)
        num //= 2
    return digits
def ans(x=0):
    answer = []
    sum = 0
    a = base10to2(x)
    for i in range(len(a)):
        if a[i] == 1 :
            answer.append(mycow[i].name)
            sum += mycow[i].weight
    #print(x,answer,a,sum)
    if sum == xx:
        return answer
    elif x == 2**n-1:
        return "not answer"
    return ans(x+1)
n = int(input('N : '))
mycow = []
for i in range(n):
    name,weight = input().split()
    mycow.append(cow(name,int(weight)))
xx = int(input('XX : '))
if isinstance(ans(),list):
    for i in ans():
        print(i,end=' ')
else:
    print(ans())'''
'''def f(n,x=0):
    so = sorted([a,b,c])
    if n == 0:
        return 1
    for i in so:
        if n >= i :
            x += f(n-i)
    return x
n = int(input('n : '))
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
print(f(n))'''
'''def f(n):
    if n == 0:
        return 1
    elif n <0:
        return 0
    return f(n-a)+f(n-b)+f(n-c)
n = int(input('n : '))
a = int(input('a : '))
b = int(input('b : '))
c = int(input('c : '))
print(f(n))'''
'''class cow:
    def __init__(self,name,weight):
        self.name = name; self.weight = weight
    def __lt__(self, other):
        return self.weight < other.weight

n = int(input('N : '))
def f(n,ans):
    if n == 0:
        return ans
    if n < 0:
        return
    for i in mycow:
        if n >= i.weight and i.name not in ans :
            ansx = ans.copy()
            ansx.append(i.name)
            run = f(n-i.weight,ansx)
            if run!= None :
                return run
mycow = []
for i in range(n):
    name,weight = input().split()
    mycow.append(cow(name,int(weight)))
xx = int(input('XX : '))
ans = []
print(f(xx,ans))'''

