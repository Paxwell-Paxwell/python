'''def countaq(r,c,ans = 0):
    if r == 0 or c == 0:
        return ans
    else:
        ans += r*c
        return countaq(r-1,c-1,ans)
r = int(input('R: '))
c = int(input('C: '))
print(countaq(r,c))'''
'''
import copy
def check(a,b):
    canmake = True
    for i in range(a,a+4):
        for j in range(b,b+2):
            if area[i][j] == '0':
                canmake = False
    return canmake
def make(a,b):
    basket = copy.deepcopy(area)
    for i in range(a, a + 4):
        for j in range(b, b + 2):
            basket[i][j] = 'x'
    areacanmake.append(basket)
def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j],end =' ')
        print()
    print()
l = int(input('Length: '))
w = int(input('Width: '))
area = []
for i in range(l):
    area.append(input().split())
areacanmake = []
for i in range(1,len(area)-4):
    for j in range(1,len(area[0])-2):
        if check(i,j):
            make(i,j)
print(f'{len(areacanmake)} possible court(s)')
for i in areacanmake:
    print_matrix(i)'''
'''
class City:
  Country = {}
  nbCity = 0
  nbCountry = 0
  def __init__(self, city, country, latitude, longitude, temperature):
    self.city = city
    self.country = country
    self.latitude = float(latitude)
    self.longitude = float(longitude)
    self.temperature = float(temperature)
    if country not in City.Country.keys():
      City.Country[country] = []
      City.nbCountry += 1
    City.Country[country].append((city, float(temperature)))
    City.nbCity += 1
def readCity():
  myCity = []
  name = input('Enter file name: ')
  with open(name) as fp:
    c = fp.readline()
    s = fp.readlines()
    for c in s:
      cc = c.strip().split(',')
      city,country,lat,long,temp = cc[0],cc[1],float(cc[2]),float(cc[3]),float(cc[4])
      myCity.append(City(city,country,lat,long,temp))
  return myCity
mycity = readCity()
conaver = {}
for i in mycity:
    if i.country not in conaver.keys():
        conaver[i.country] = [i.temperature]
    else:
        conaver[i.country].append(i.temperature)
for k,v in conaver.items():
    aver = sum(v)/len(v)
    print(f'{k} {aver:.2f}')'''
'''
class Country:
  nbCountry = 0
  def __init__(self, country, population, EU,coastline):
    self.country = country
    self.population = float(population)
    self.EU = EU
    self.coastline = coastline
    Country.nbCountry += 1

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
  name = input('Enter city file: ')
  with open(name) as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      city,country,lat,long,temp = cc[0],cc[1],float(cc[2]),float(cc[3]),float(cc[4])
      myCity.append(City(city,country,lat,long,temp))
  return myCity
def readCountry():
  myCountry = []
  name = input('Enter country file: ')
  with open(name) as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      country,population,EU,coastline = cc[0], cc[1], cc[2], cc[3]
      myCountry.append(Country(country,population,EU,coastline))
  return myCountry
def q01(myCity, myCountry):
  countryeunotco = []
  for i in myCountry:
    if i.EU == 'no' and i.coastline =='yes':
      countryeunotco.append(i.country)
  averrangetem = {}
  for i in myCity:
    if i.country in countryeunotco:
      if i.country not in averrangetem.keys():
        averrangetem[i.country] = [i.temperature]
      elif i.country in averrangetem.keys():
        averrangetem[i.country].append(i.temperature)
  for k in averrangetem.keys():
    aver = sum(averrangetem[k])/len(averrangetem[k])
    averrangetem[k] = aver
    sorted_con ={}
    for i in sorted(averrangetem.items(),key = lambda x:x[0]):
        sorted_con[i[0]] = i[1]
  for k,v in sorted_con.items():
    print(f'{k} {v:.2f}')
myCity = readCity()
myCountry = readCountry()
print('Average temperature of countries having coastline, but not in EU:')
q01(myCity,myCountry)'''
'''
n = int(input('Input n: '))
m = int(input('Input m: '))
def found(i,m,place = []):
    for j in m:
        if isinstance(j,list):
            nplace = place.copy()
            nplace.append(m.index(j))
            c = found(i,j,nplace)
            if c != None:
                return c
        elif j == i:
            place.append(m.index(i))
            c = place
            return c
num = []
position = []
for i in range(n):
    a = [int(j) for j in input().split()]
    position.append(a)
    num += a
num.sort()
for i in num:
    a=tuple(found(i,position))
    print(f'({a[0]},{a[1]})')
'''
'''
def printmat(mat):
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      print(mat[i][j], end = " ")
    print()
m = int(input('M: '))
n = int(input('N: '))
num = []
for i in range(m):
    num.append([int(i) for i in input().split()])
print('sorted matrix is:')
setnum = []
position = []
for i in range(1,m+1):
    x, y = m - i, 0
    add = []
    if i >= n:
       i = n
    for j in range(1,i+1):
        position.append((x,y))
        add.append(num[x][y])
        if j != i:
            x += 1
            y += 1
    y = 0
    if i != m:
        x -= i
    add.sort()
    setnum += add
for i in range(n-1,0,-1):
    x, y = 0, n-i
    add = []
    for j in range(1, i + 1):
        position.append((x,y))
        add.append(num[x][y])
        if j != i:
            x += 1
            y += 1
    add.sort()
    setnum+= add
for i in range(len(position)):
    a = position[i]
    num[a[0]][a[1]] = setnum[i]
printmat(num)
'''
n = int(input('N: '))
def choice(a,b,c):
    size = [a,b,c]
    size.sort()
    if size[0] <= 8 and size[1] <= 10 and size[2] <= 15:
        box[0] += 1
        print('Box size 1')
    elif size[0] <=12 and size[1] <= 15 and size[2] <= 25:
        box[1] += 1
        print('Box size 2')
    elif size[0] <=20 and size[1] <= 40 and size[2] <= 50:
        box[2] += 1
        print('Box size 3')
    else:
        print('Oversize product')

box = [0,0,0]
j = 1
for i in range(n):
    a = int(input(f'Order {j} A: '))
    b = int(input(f'Order {j} B: '))
    c = int(input(f'Order {j} C: '))
    j += 1
    choice(a,b,c)
print(f'Use Box size 1: {box[0]}')
print(f'Use Box size 2: {box[1]}')
print(f'Use Box size 3: {box[2]}')


