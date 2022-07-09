#w1
'''def AmHere(name) :
    print('Hello !!!')
    print(f"I'm here {name}!!!")
name = input('Who are you going to call : ')
AmHere(name)'''
#w2
'''import math
hmp = int(input('How many Pi : '))
for i in range(hmp) :
    print(math.pi)'''
#w3
'''import math
d= int(input('Degree : '))*(math.pi/180)
print(f'sin : {math.sin(d):.2f}')
print(f'cos : {math.cos(d):.2f}')
print(f'tan : {math.tan(d):.2f}')'''
#5
'''x = input("Enter string : ")
print(f"align --- {x:>20} --- right")
print(f"align --- {x:<20} --- left")
print(f"align --- {x:^20} --- center")'''
#6
'''str = input('Dak fung : ')
if  "i know i'm bad" in str :
    print('Find!!!')
else :
    print('Not Find...')'''
#7
'''str = input()
for i in str :
    if (ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) :
        k = i
    else :
        k = i
        break
if str[0].upper() == k.upper() :
    print('YES')
    print(str[0].upper())
else :
    print('NO')'''
#hw1
'''
import math
def inputShape() :
    s = int(input('Input Shape: '))
    return s
def calculatePrice(v) :
    b = int(input(f'Price(Bath) per 1 cubic meter: '))
    print(f'The price is {v*b:.2f} Baht.')
    return v
def calculateSphere() :
    r = int(input('Input radius(meter): '))
    v = (4/3)*math.pi*r**3
    print(f'The volume is {v:.2f} cubic meter.')
    return v
def calculateCone() :
    r = int(input('Input radius(meter): '))
    h=  int(input('Input height(meter): '))
    v = math.pi*r**2*h/3
    print(f'The volume is {v:.2f} cubic meter.')
    return v
def calculateCylinder() :
    r = int(input('Input radius(meter): '))
    h = int(input('Input height(meter): '))
    v = math.pi * r ** 2 * h
    print(f'The volume is {v:.2f} cubic meter.')
    return v
def calculatePrism() :
    w = int(input('Input width(meter): '))
    l = int(input('Input length(meter): '))
    h = int(input('Input height(meter): '))
    v = w*l*h
    print(f'The volume is {v:.2f} cubic meter.')
    return v
def calculatePyramid() :
    w = int(input('Input width(meter): '))
    l = int(input('Input length(meter): '))
    h = int(input('Input height(meter): '))
    v = w*l*h/3
    print(f'The volume is {v:.2f} cubic meter.')
    return v
x = inputShape()
if x == 1:
    v = calculateSphere()
elif x == 2:
    v = calculateCone()
elif x == 3:
    v = calculateCylinder()
elif x == 4:
    v = calculatePrism()
else :
    v = calculatePyramid()
calculatePrice(v)'''
#hw2
'''def Head(n) :
    print('','o'*n)
    for i in range(n//2-1) :
        print(' o'+' '*((n//2-1)*2)+'o')
    print('','o' * n)
def Body(n) :
    for i in range(n//2-1) :
        print(' '*(n//2)+'||')
    print('-'*(n//2)+'||'+'-'*(n//2))
    for i in range(n//2-1) :
        print(' '*(n//2)+'||')
def Leg(n) :
    for i in range(n//2) :
        print(' '*(n//2-i)+'/'+'  '*i+'\\')
n = int(input())
Head(n)
Body(n)
Leg(n)'''
#hw3
'''def Head(n) :
    print(' '*(n-1)+'*'*n)
    for i in range(n-2) :
        print(' '*(n-1)+'*'+' '*(n-2)+'*')
    print(' '*(n-1)+'*'*n)
def Hand(n) :
    for i in range(1,n) :
        print(' '*(i-1)+'*'+' '*(2*(n-1-i)+n)+'*')
def Leg(n) :
    for i in range(1,n) :
        print(' '*(n-i-1)+'*'+' '*(2*(i-1)+n)+'*')
def draw(n) :
    Hand(n)
    Head(n)
    Leg(n)

n = int(input())
draw(n)'''
#hw 4
'''def even_check(num):
    if num%2 == 0:
         x = 'even'
    else :
         x = 'odd'
    print(f'The number is {x}')
    return x
def prime_check(num) :
    if  num == 1 :
        print(f'The number is not prime')
    else :
        if num == 2 :
            print('The number is prime')
        for i in range(2,num) :
            if num%i == 0 :
                print('The number is not prime')
                break
            elif i == num-1:
                print('The number is prime')

num = int(input('Number : '))
even_check(num)
prime_check(num)'''
#hw 5'''
'''def What(str) :
    for i in str :
        if ord(i)>=65 and ord(i) <= 90 :
            return 'Photobook'
        else :
            return 'Album'
def SStatus() :
    return status
def RReal(str) :
    if ord(str[0])-ord(str[-1]) == -1:
        return 'True'
    else :
        return 'False'
str = input()
status = What(str)
print(SStatus())
print(RReal(str))'''

# hw 6
'''def plus(total,value) :
    return total+value
def minus(total,value) :
    return total-abs(value)
r = int(input('How many food you have : '))
total = 0
for i in range(r) :
    str = input()
    a,b = str.split(' ')
    c = int(a)*int(b)
    if c > 0 :
        total = plus(total,c)
    else :
        total = minus(total,c)
print(total)'''
'''import math
d = int(input())
for i in range(d-1,-1,-1):
    for y in range(i+1):
        print(int(math.factorial(i)/(math.factorial(i-y)*math.factorial(y))),end=' ')
    print('')'''


