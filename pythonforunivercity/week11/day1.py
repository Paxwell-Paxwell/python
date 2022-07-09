'''import json


class Account:
    def __init__(self, name, accnb, money, history):
        self.name = name;
        self.accnb = accnb;
        self.money = money
        self.history = history

    def __str__(self):
        return f'Name : {self.name}\nAccount number : {self.accnb}\nMoney : {self.money}'

    def show_data(self):
        print(self.__str__())
        if self.history['deposit'] == 0 and self.history['withdraw'] == 0:
            print('History')
        else:
            print(f'History : Deposit : {self.history["deposit"]}\nWithdraw : {self.history["withdraw"]}')


def readJsonData():
    myAccount = []
    ss = json.loads(s)
    for i in range(len(ss)):
        # print(ss[i])
        name, accNb, money, history = ss[i]['name'], ss[i]['account number'], ss[i]['money'], ss[i]['history']
        a = Account(name, accNb, money, history)
        myAccount.append(a)
        # print(a)
    return myAccount


def menuOne(myAccount):
    accNb = input('Account number : ')
    for m in myAccount:
        if m.accnb == accNb:
            m.show_data()
'''
'''import csv
maxx = -1
minn = 1e9
class classes:
    def __init__(self,idd,gender,race_ethnicity,parental_level_of_education,
                 lunch,test_preparation_course,math_score,reading_score,writing_score):
        self.idd = idd
        self.gender = gender; self.race_ethnicity = race_ethnicity
        self.parental_level_of_education= parental_level_of_education
        self.lunch =lunch ; self.test_preparation_course=test_preparation_course
        self.math_score = math_score ; self.reading_score = reading_score
        self.writing_score = writing_score
    def show_data(self):
        print(f'gender : {self.gender}')
        print(f'race/ethnicity : {self.race_ethnicity}')
        print(f'parental level of education : {self.parental_level_of_education}')
        print(f'lunch : {self.lunch}')
        print(f'test preparation course : {self.test_preparation_course}')
        print(f'math score : {self.math_score}')
        print(f'reading score : {self.reading_score}')
        print(f'writing score : {self.writing_score}')
    def less_from_max_reading_score(self):
        print(f'less than max : {maxx-int(self.math_score)}')
    def more_from_max_reading_score(self):
        print(f'less than max : {int(self.math_score)-minn}')
    def can_pass(self):
        sum_score = self.math_score+self.writing_score+self.reading_score
        if sum_score > 240 :
            print('Can pass')
        else:
            print('Can\'t pass')
    def __str__(self):
        return f'math score : {self.math_score}, reading score : {self.reading_score}, writing score : {self.writing_score}'
def choose(num,id):
    if num == 1:
        dataclasses[id-1].show_data()
    elif num == 2:
        dataclasses[id-1].less_from_max_reading_score()
    elif num ==3:
        dataclasses[id-1].more_from_max_reading_score()
    elif num ==4:
        dataclasses[id-1].can_pass()
    elif num == 5:
        print(dataclasses[id-1])
def read_csv(filename):
    with open(filename) as f:
        global maxx , minn
        datas = csv.reader(f)
        data = [ i for i in datas]
        for i in range(1,len(data)) :
            maxx = max(maxx,int(data[i][6]))
            minn = min(minn,int(data[i][7]))
    return data
filename = input('Filename : ')
menu = int(input('Menu : '))
id = int(input('ID : '))
dataclasses = []
with open(filename.strip()) as f:
    h = f.readline()
    s = f.readlines()
for i in s:
    a = i.strip().split(',')
    add = []
    for j in a[1:]:
        add.append(j)
    dataclasses.append(classes(add[0],add[1],add[2],add[3],add[4],add[5],add[6],add[7]))
read_csv(filename)
choose(menu,id)'''
'''
import csv
maxx = -1
minn = 1e9

def read_csv(filename):
    with open(filename) as f:
        global maxx , minn
        datas = csv.reader(f)
        data = [ i for i in datas]
        for i in range(1,len(data)) :
            maxx = max(maxx,int(data[i][6]))
            minn = min(minn,int(data[i][7]))
    return data
class Std:
    def __init__(self,id,gender,race_ethnicity,parental_level_of_education,
                 lunch,test_preparation_course,math_score,reading_score,writing_score):
        self.id = id
        self.gender = gender; self.race_ethnicity = race_ethnicity
        self.parental_level_of_education= parental_level_of_education
        self.lunch =lunch ; self.test_preparation_course=test_preparation_course
        self.math_score = math_score ; self.reading_score = reading_score
        self.writing_score = writing_score
    def show_data(self):
        print(f'gender : {self.gender}')
        print(f'race/ethnicity : {self.race_ethnicity}')
        print(f'parental level of education : {self.parental_level_of_education}')
        print(f'lunch : {self.lunch}')
        print(f'test preparation course : {self.test_preparation_course}')
        print(f'math score : {self.math_score}')
        print(f'reading score : {self.reading_score}')
        print(f'writing score : {self.writing_score}')
    def less_from_max_math_score(self):
        print(f'less than max : {maxx-int(self.math_score)}')
    def more_from_min_reading_score(self):
        print(f'more than min : {int(self.reading_score)-minn}')
    def can_pass(self):
        sum_score = int(self.math_score)+int(self.writing_score)+int(self.reading_score)
        if sum_score > 240 :
            print('Can pass')
        else:
            print('Can\'t pass')
    def __str__(self):
        return f'math score : {self.math_score}, reading score : {self.reading_score}, writing score : {self.writing_score}'

filename = input("Filename : ")
datas = read_csv(filename)
classes = list()
for i in range(1,len(datas)) :
    data = Std(datas[i][0],datas[i][1],datas[i][2],datas[i][3],datas[i][4],datas[i][5],datas[i][6],datas[i][7],datas[i][8])
    classes.append(data)


menu = int(input("Menu : "))
id = input("ID : ")
for i in classes :
    if i.id == id :
        if menu == 1 : # show data
            i.show_data()
        elif menu == 2 : # less_from_max_math_score
            i.less_from_max_math_score()
        elif menu == 3 : # more_from_min_reading_score
            i.more_from_min_reading_score()
        elif menu == 4: # can_pass
            i.can_pass()
        elif menu == 5: # print
            print(i)
        break
'''
'''
import json
class Account:
    def __init__(self, name, accnb, money, history):
        self.name = name
        self.accnb = accnb
        self.money = money
        self.history = history
    def __str__(self):
        return f'Name : {self.name}\nAccount number : {self.accnb}\nMoney : {self.money}'

    def show_data(self):
        print(self.__str__())
        if self.history['deposit'] == 0 and self.history['withdraw'] == 0:
            print('History :')
        else:
            print(f'History : Deposit : {self.history["deposit"]}\nWithdraw : {self.history["withdraw"]}')
    def deposit(self):
        amount = int(input('Amount : '))
        self.history["deposit"] += amount
        self.money +=  amount
        print(f'Current money : {self.money}')
    def withdraw(self):
        amount = int(input('amount : '))
        self.history["withdraw"] += amount
        self.money -= amount
        print(f'Current money : {self.money}')
    def show_history(self):
        if self.history["deposit"] > 0:
            print(f'Deposit : {self.history["deposit"]}')
        if self.history["withdraw"]>0:
            print(f'Withdraw : {self.history["withdraw"]}')

def readJsonData():
    classes = []
    ss = json.loads(s)
    for i in range(len(ss)):
        # print(ss[i])
        name, accNb, money, history = ss[i]['name'], ss[i]['account number'], ss[i]['money'], {'deposit': 0,'withdraw': 0}
        a = Account(name, accNb, money, history)
        classes.append(a)
        # print(a)
    return classes

def choose(num):
    global ac
    if num == 1:
        ac.show_data()
    elif num == 2:
        ac.deposit()
    elif num ==3:
        ac.withdraw()
    elif num ==4:
        ac.show_history()
    elif num == 5:
        an = input('Account number : ')
        for i in classes:
            if i.accnb == an:
                ac = i
                break
def menuOne(myAccount):
    accNb = input('Account number : ')
    for m in myAccount:
        if m.accnb == accNb:
            m.show_data()
filename = input('Filename : ')
with open(filename) as f:
    s = f.read()
classes = readJsonData()
an = input('Account number : ')
for i in classes:
    if i.accnb == an:
        ac = i
        break
while True:
    num = int(input('Menu : '))
    if num == 0:
        break
    choose(num)'''
'''
class Run:
    def __init__(self,name,_range,velocity,response):
        self.name = name; self._range =_range
        self.velocity =velocity; self.response = response
        self.time()
    def time(self):
        num =0
        for i in range(len(self._range)):
            if distance >= self._range[i]:
                num +=1
        num -= 1
        time = 0
        for i in range(num):
            time += (self._range[i+1]-self._range[i])/self.velocity[i]
        time += (distance-self._range[num])/self.velocity[num]
        self.time = float(f"{time:.2f}")
        return self.time
    def __lt__(self, other):
        if self.time != other.time:
            return self.time<other.time
        else:
            if self.response != other.response:
                return self.response > other.response
            else:
                return self.name<other.name
    def __str__(self):
        return f'{self.name} {self.time:.2f}'

import json
filename = input('Enter json filename : ')
distance = int(input('Enter distance (meter) : '))
with open(filename) as f:
    data = json.loads(f.read())
Runner = []
for i in data['racer'] :
    name,_range,velocity,response = i['name'],i['_range'],i['velocity'],i['response']
    Runner.append(Run(name,_range,velocity,response))
Runner.sort()
for i in Runner:
    print(i)'''
'''
class Product:
    def __init__(self,id,name,price):
        self.id = id; self.name = name
        self.price = price
def choose(num):
    global id
    if num == 1:
        print(p.name)
    elif num == 2:
        print(p.price)
    else:
        while True:
            id = input('Id : ')
            if id in [i.id for i in pro]:
                break
            else:
                print('This id doesn\'t exist.')

num= int(input('How many products are there? : '))
pro = []
for i in range(num):
    a = input().split(' ')
    pro.append(Product(a[0],a[1],a[2]))
while True:
    id = input('Id : ')
    if id in [i.id for i in pro]:
        break
    else :
        print('This id doesn\'t exist.')
while True:
    Q = int(input('Q : '))
    if Q == 0:
        break
    for i in pro:
        if i.id == id:
            p = i
            break
    choose(Q)
    '''
#shape
'''
import math
class Rectangle:
    def __init__(self,l,w):
        self.l = l ; self.w = w
    def area(self):
        return self.l*self.w
    def perimeter(self):
        return 2*(self.l+self.w)
    def is_square(self):
        if self.w == self.l:
            return 'This rectangle is square too.'
        else :
            return 'This rectangle is not square.'
class Triangle:
    def __init__(self,l1,l2,l3):
        self.l1 =l1; self.l2 = l2
        self.l3 =l3
    def area(self):
        s = (self.l1 +self.l2 + self.l3)/2
        area = math.sqrt(s*(s-self.l1)*(s-self.l2)*(s-self.l3))
        return area
    def perimeter(self):
        return self.l1+self.l2+self.l3
    def is_right_triangle(self):
        side = [self.l1,self.l2,self.l3]
        side.sort()
        if self.l1**2+self.l2**2 == self.l3**2:
            return 'This triangle is right triangle too.'
        else:
            return 'This triangle is not right triangle.'
class Circle:
    def __init__(self,r):
        self.r = r
    def perimeter(self):
        return 2*pi*self.r
    def area(self):
        return pi*self.r**2
pi =3.14
l = int(input("Enter rectangle length : "))
w = int(input("Enter rectangle width : "))
p1 = Rectangle(l,w)
print(f'Area is {p1.area()}.')
print(f'Perimeter is {p1.perimeter()}.')
print(p1.is_square())

l1 = int(input("Enter triangle first side length : "))
l2 = int(input("Enter triangle second side length : "))
l3 = int(input("Enter triangle third side length : "))
p2 = Triangle(l1,l2,l3)
print(f'Area is {p2.area()}.')
print(f'Perimeter is {p2.perimeter()}.')
print(p2.is_right_triangle())

r = int(input("Enter circle radius : "))
p3 = Circle(r)
print(f'Area is {p3.area()}.')
print(f'Perimeter is {p3.perimeter()}.')'''
'''import math
class MyMath:
    def is_even(self,num) :
        if num%2 ==0 :
            return True
        else:
            return False
    def fac(self,num):
       return math.factorial(num)
    def ten_to_bi(self,num):
        if num == 0:
            return [0]
        digits = []
        while num:
            a = num%2
            if a >= 10:
                a = chr(a+55)
            digits.append(str(a))
            num //= 2
        base = ''
        for i in digits[::-1]:
            base += i
        return base
    def ten_to_oct(self,num):
        if num == 0:
            return [0]
        digits = []
        while num:
            a = num%8
            if a >= 10:
                a = chr(a+55)
            digits.append(str(a))
            num //= 8
        base = ''
        for i in digits[::-1]:
            base += i
        return base

    def ten_to_sixteen(self,num):
        if num == 0:
            return [0]
        digits = []
        while num:
            a = num % 16
            if a >= 10:
                a = chr(a + 55)
            digits.append(str(a))
            num //= 16
        base = ''
        for i in digits[::-1]:
            base += i
        return base
    def is_prime(self,num):
        if num%2 == 0 or num == 1:
            return False
        else :
            for i in range(3,round(num/2)+1,2):
                b = i
                if num%i ==0:
                    return False
            if b == round(num/2)-1:
                return True
    def divide_by(self,num,k):
        if num%k == 0:
            return True
        else:
            return False
    def int_to_roman(self,num):
        intToroman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
                      50: 'L', 90: 'XC', 100: 'C', 400: 'XD', 500: 'D', 900: 'CM', 1000: 'M'}
        print_order = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman = ''
        for x in print_order:
            if num != 0:
                quotient = num // x
                if quotient != 0:
                    for y in range(quotient):
                        roman += intToroman[x]
                num = num % x
        return roman
    def pi(self):
        nipi = 3
        for k in range(50):
            nipi += 4*((-1)**k/((2*k+2)*(2*k+3)*(2*k+4)))
        return nipi
    def __init__(self):
        self.pi = self.pi()
my_math = MyMath()
num = int(input("Please Enter Number : "))
k = int(input("Divide by? : "))

if my_math.is_even(num):
    print('This number is even number.')
else:
    print('This number is not even number.')

if num <= 20:
    print(f'factorial is {my_math.fac(num):,.0f}.')
else:
    print('factorial TOO LONG')

if my_math.is_prime(num):
    print('This number is a prime number.')
else:
    print('This number is not a prime number.')

if(my_math.divide_by(num,k)):
    print(f'{num} is divisible by {k}')
else:
    print(f'{num} is not divisible by {k}')

print(f'{num} is {my_math.ten_to_bi(num)} in base 2.')
print(f'{num} is {my_math.ten_to_oct(num)} in base 8.')
print(f'{num} is {my_math.ten_to_sixteen(num)} in base 16.')
print(f'{num} is {my_math.int_to_roman(num)} in roman numeral system.')
print(f'PI is {my_math.pi:.20f}')'''
'''
class Matrix:
    def __init__(self,matrix):
        self.matrix = matrix
    def det(self):
        a = self.matrix
        diction1 = a[0][0]*a[1][1]*a[2][2]+a[0][1]*a[1][2]*a[2][0]+a[0][2]*a[1][0]*a[2][1]
        diction2 = a[2][0]*a[1][1]*a[0][2]+a[2][1]*a[1][2]*a[0][0]+a[2][2]*a[1][0]*a[0][1]
        return diction1-diction2
    def plus(self,other):
        sumAB = []
        for x in range(len(self.matrix)):
            add = []
            for y in range(len(self.matrix[0])):
                add.append(self.matrix[x][y] + other.matrix[x][y])
            sumAB.append(add)

        return Matrix(sumAB)
    def minus(self,other):
        miAB = []
        for x in range(len(self.matrix)):
            add = []
            for y in range(len(self.matrix[0])):
                add.append(self.matrix[x][y] - other.matrix[x][y])
            miAB.append(add)

        return Matrix(miAB)
    def multiply(self,other):
        mulAB = []
        A = self.matrix ; B= other.matrix
        for x in range(len(A)):
            add = []
            for z in range(len(B[0])):
                msum = 0
                for y in range(len(A[0])):
                    msum += A[x][y] * B[y][z]
                add.append(msum)
            mulAB.append(add)
        return Matrix(mulAB)
    def show(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                print(f'{self.matrix[i][j]:^6}', end=' ')
            print()
def input_matrix():
    data = []
    for i in range(3):
        data.append([int(j) for j in input(f"Row {i+1} : ").split()])
    return data
print("input row of matrix A")
A = Matrix(input_matrix())
print("input row of matrix B")
B = Matrix(input_matrix())

print(f'Det of Matrix(A) = {A.det()}')
print(f'Det of Matrix(B) = {B.det()}')

print("Matrix(A+B) is:")
res = A.plus(B)
res.show()

print("Matrix(A-B) is:")
res = A.minus(B)
res.show()

print("Matrix(A*B) is:")
res = A.multiply(B)
res.show()
'''
'''
class py_solution :
    def __init__(self,word):
        self.word = word
    def is_valid_parentheses(self):
        cha = []
        check = {'{':'}','[':']','(':')'}
        newword = ['','']
        for i in self.word:
            cha.append(i)
        if len(cha)%2 ==1:
            return False
        for i in cha:
            if i in check.keys():
                newword[0] += i+check[i]
        add = []
        key =''
        for i in cha:
                if i in check.keys():
                    key += i
                else:
                    if key != '':
                        add.append(key)
                    key = ''
        for j in range(len(add)):
            for i in range(len(add[j])-1,-1,-1):
                add[j] += check[add[j][i]]
        for i in add:
            newword[1] += i
        if self.word in newword:
            return True
        else:
            return False
word = input('input: ')
a = py_solution(word)
if a.is_valid_parentheses():
    print('valid parentheses')
else:
    print('invalid parentheses')
'''
'''
import numpy as np
X = np.random.RandomState(1)
class Game:
    combo = 0
    def __init__(self,blood):
        self.blood =blood
    def player_choose_skill(self):
        skill = input('Attack(a) or Heal(h): ')
        if skill == 'a':
            self.base_damage = 10 + Game.combo*2
            monster.blood -= self.base_damage
            if monster.blood < 0:
                monster.blood = 0
            print(f'Monster\'s HP left {monster.blood}')
            Game.combo += 1
        else:
            Game.combo = 0
            self.blood += 20
            print(f'Your HP left {self.blood}')
    def moster_attack(self,player):
        self.base_attack = X.randint(1, 40)
        player.blood -= self.base_attack
        if player.blood <0:
            player.blood = 0
        print(f'Monster\'s turn : Your HP left {player.blood}')
def whowin():
    if monster.blood <= 0 or player.blood <= 0:
        if monster.blood <= 0:
            print('You win.(^_^)')
            return 0
        else:
            print('You lose and die.(T_T)')
            return 0
blood_start = int(input('Blood Start: '))
player = Game(blood_start)
monster = Game(blood_start)
while True :
    player.player_choose_skill()
    a = whowin()
    if a == 0:
        break
    monster.moster_attack(player)
    a = whowin()
    if a == 0:
        break'''
import numpy as np
X = np.random.RandomState(1)
class Game:
    def __init__(self,blood,speed):
        self.hp = blood; self.speed = speed
    def __lt__(self, other):
        return self.speed < other.speed
class Player(Game):
    combo =  0
    def __init__(self, blood, speed,id):
        super().__init__( blood, speed)
        self.id = id
    def player_choose_skill(self,monster):
        skill = input('Attack(a) or Heal(h): ')
        if skill == 'a':
            self.base_damage = 10 + Player.combo*2
            monster.hp -= self.base_damage
            Player.combo += 1
            if monster.hp <= 0:
                monster.hp = 0
            return skill
        else:
            Player.combo = 0
            self.hp += 20*number_mon
            return skill
class Monster(Game):
    def __init__(self,id,blood,speed):
        self.speed = speed
        self.hp = int(blood/number_mon)
        self.id = id
    def moster_attack(self):
        self.base_attack = X.randint(1, 40)
        player.hp -= self.base_attack
        if player.hp <= 0:
            player.hp = 0

blood_start = int(input('Blood Start: '))
your_speed = int(input('Your speed: '))
player = Player(blood_start,your_speed,'player')
number_mon = int(input('Number of monsters: '))
speed = [player]
for i in range(number_mon):
    speed.append(Monster(i+1,blood_start,int(input(f'Monster {i+1} speed: '))))
speed.sort(reverse=True)
r = 1
b = True
while b :
    print('=========================')
    print(f'Turn {r}')
    print('-------------------------')
    for i in speed:
        #print(i.id)
        if  i.id != 'player' and i.hp != 0:
            i.moster_attack()
            print(f'- Monster {i.id} Turn -')
            print(f'Your HP left {player.hp}')
            if player.hp == 0:
                print('You lose and die.(T_T)')
                b = False
                break
        elif i.id == 'player':
            print('- Your Turn -')
            for j in speed:
                if j.id != 'player':
                    lastmon = j
            for j in speed:
                if j.id != 'player' and j.hp != 0 :
                    atmon = j
                    break
            skill = i.player_choose_skill(atmon)
            if skill == 'a':
                print(f'Monster {atmon.id} HP left {atmon.hp}')
            else :
                print(f'Your HP left {player.hp}')
            if atmon.hp == 0 and atmon == lastmon:
                print('You win.(^_^)')
                b= False
                break
    r += 1