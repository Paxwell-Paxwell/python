'''def calAmount(a,b,c) :
    return a*(1+b/100)**c
a = int(input('Enter initial amount in Baht: '))
b = int(input('Enter interest rate in percent: '))
print(f'Total amount after 1 year is {calAmount(a,b,1):.2f} Baht.')
print(f'Total amount after 5 years is {calAmount(a,b,5):.2f} Baht.')
print(f'Total amount after 10 years is {calAmount(a,b,10):.2f} Baht.')
print(f'Total amount after 20 years is {calAmount(a,b,20):.2f} Baht.')'''
#2
'''def trapezoid(side1,side2,height):
    area = (side1+side2)/2 *height
    return area
print("Please specify your trapezoid's properties.")
side1 = float(input('Enter length of parallel side 1: '))
side2 = float(input('Enter length of parallel side 2: '))
height = float(input('Enter height: '))
print(f'Trapezoid\'s area is {trapezoid(side1,side2,height):.2f}')'''
#3
'''tv = int(input('How many TVs do you want? '))
dvd = int(input('How many DVD players do you want? '))
au = int(input('How many audio systems do you want? '))
total = tv*12000+dvd*3000+au*6000
dis = 0
print(f'The total amount is {total:.2f} baht.')
if total >= 40000:
    dis = 0.15*total
    print(f'Discount: {dis:.2f} baht.')
total = total - dis
print(f'Your payment is {total:.2f} baht. Thank you.')
'''
#4
'''import sys
import cmath
a = float(input('1st coefficient: '))
if a == 0:
    sys.exit('1st coefficient can\'t be zero. Program exits.')
b = float(input('2nd coefficient: '))
c = float(input('3rd coefficient: '))
D = b**2 - 4*a*c
r1 = -1*b/(2*a) +cmath.sqrt(D)/(2*a)
r2 = -1*b/(2*a) -cmath.sqrt(D)/(2*a)
if D > 0 :
    print(f'There are two real roots: {r1.real:.3f} and {r2.real:.3f}')
elif D<0 :
    print(f'There are two complex roots: {r2.real:.3f}+{abs(r2.imag):.3f}i and {r1.real:.3f}-{abs(r1.imag):.3f}i')
else :
    print(f'Only one real root: {r1.real:.3f}')
'''

#5
'''def total_score(hw,mid,fi) :
    total = hw*0.1 + mid*0.4 +fi*0.5
    return total
def grade(s) :
    if s >= 80 :
       return 'A'
    elif s>= 75 :
       return 'B+'
    elif s>= 70 :
       return 'B'
    elif s>= 65 :
       return 'C+'
    elif s>= 60 :
       return 'C'
    elif s>= 55 :
       return 'D+'
    elif s>= 50 :
       return 'D'
    else :
       return 'F'
hw = int(input('What is the homework percentage? '))
mid = int(input('What is the midterm percentage? '))
fi = int(input('What is the final percentage? '))
total = total_score(hw,mid,fi)
print(f'Total score: {total:.2f}')
print(f'Your grade is {grade(total)}')'''
#6
'''str = input('What is your message? ')
for i in range(len(str)):
    print(' '*i+str[i])'''
#7
'''def pattern(p):
    if p ==1 :
        for i in range(1,n+1) :
            print(c*i)
    elif p == 2:
        for i in range(n,0,-1) :
            print(c*i)
    elif p == 3:
        for i in range(1,n+1) :
            print(f'{c*i:>{n}}')
    else :
        for i in range(n,0,-1):
            print(f'{c*i:>{n}}')
p = int(input('pattern: '))
c = input('char: ')
n = int(input('n: '))
pattern(p)'''
#8
'''sump = 0
sumn = 0
while True:
    x = float(input('Enter a number (to exit, just enter 0): '))
    if x>0 :
        sump += x
    elif x<0 :
        sumn += x
    else :
        break
print(f'Sum of all positive numbers is {sump:.2f}')
print(f'Sum of all negative numbers is {sumn:.2f}')'''
#9
'''import sys
h = int(input('What is the well\'s depth? '))
j = int(input('Enter the height the frog can jump up: '))
d = int(input('Enter the height the frog slips down: '))
if h == j :
    print(f'The frog is free on day 1.')
    sys.exit()
if not ( j > d ):
    sys.exit('The frog cannot get out of the well.')
fd = h
day = 0
while fd>0 :
    day += 1
    fd  -= j
    if not fd>0:
        continue
    print(f'On day {day} the frog leaps to the depth of {fd} meters.')
    fd += d
    print(f'At night he slips down to the depth of {fd} meters.')
print(f'The frog is free on day {day}.')'''
#10
'''l = int(input('Enter number of levels: '))
b = int(input('How big is each bush? '))
for i in range(l):
    for y in range(b):
        print(f"{'*'*(1+2*y):^{1+2*(b-1)}}")'''
#10
def check(a,b,c):
    if  a<=15 and b <= 10 and c<= 8:
        print('Box size 1')
    elif a<=25 and b<= 15  and c<=12 :
        print('Box size 2')
    elif a<=50 and b<= 40 and c<= 20:
        print('Box size 3')
    else:
        print('Oversize product')

a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
check(a,b,c)