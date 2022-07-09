# No.1
'''pole = int(input('number of electric poles : '))
max = 0
max2 = 0
for i in range(pole):
    cost = int(input())
    if cost >= max :
        max = cost
    elif cost >= max2:
        max2 = cost
time = max//max2
if time >= 3 :
    print('YES')
    print(max)
else :
    print('NO')'''
# No.2
'''Ds = int(input("Input distance(kilometer): "))
t=0
if Ds >= 6:
    t = Ds//6
    if t == Ds/6 :
        t =t-1
st = Ds*10 + t*10
print(f'It takes {st//60} hours and {st-(st//60)*60 } minutes to reach the destination.')
'''
#3
'''s = 0
n=1
cd = 100
while True :
    d = int(input('Input distance: '))
    s = s + d
    cd= cd+2**n
    n = n+1
    print(f'Police distance: {s}')
    print(f'Criminal distance: {cd}')
    if s >= cd :
        print('Caught him!')
        break'''
#4
'''r = int(input())
for i in range(r):
    print('O'*(i+1))'''
#5
'''t = int(input('s: '))
h = t//3600
m = t//60 - (t//3600)*60
s = t%60
print(f'{t} seconds equals {h} hour(s) {m} minute(s) and {s} second(s)')'''
#6
'''md = int(input('How many day : '))
cost = 0
for i in range(md):
    price = float(input(f'Input price in day {i+1} : '))
    if i == 0 :
        price = 0.95*price
    else :
        price = (0.95-(0.01*i))*price
    cost = price +cost
cost = '{0:.2f}'.format(cost)
print(f'Summary price = {cost}')'''
#7
'''t = int(input('How long have Buzz played ?: '))
h = t//60
m = t%60
if m > 20 :
    h = h+1
price = h*900
if h >= 1 and h<2 :
        price = price
        print(f'Total price is {round(price)} baht.')
elif h >=2 and h<4 :
        price = 0.9 * price
        print(f'Total price is {round(price)} baht.')
elif h >=4 and h<5 :
        price = 0.8 * price
        print(f'Total price is {round(price)} baht.')
else :
        price = 0.7 * price
        print(f'Total price is {round(price)} baht.')'''
#8
'''ij = input("Is Bulotelli injuredy(y/n) ")
if ij == 'y' :
        print('Not available')
else :
        lt = input('Is Bulotelli late for the training?(y/n) ')
        if lt == 'y' :
                dw = input('Did Bulotelli perform well in training?(y/n) ')
            if dw == 'y':
                        print('Substitute')
            else :
                        print('Not selected')
        else :
                print('Starter')'''
'''num = int(input())
a = input('Arrow : ')
b = input('Stick : ')
x = a
for i in range(num)  :
  print(" "*(num-i-1),x)
  x = x+ 2*a
for  i in range(num)  :
   print(" "*(num-1),b)'''
''''#hw 2 no2
x = int(input())
y = int(input())
d = int(input())
i = 1
while x <= y :
   if  x%d == 0:
        x=x+11
        if x%d != 0:
           if x >y :
               break
           print(x, end=' ')
           x=x+1
   elif x%d != 0 :
        print(x,end=' ')
        x = x + 1
   if i%10 == 0  :
        print(end ='\n')
   i = i+1'''
# hw2 n03
'''def polehigh(d,c):
        if time >= 3:
            p้rint(f'Avg : {aver}')
            if aver <= c:
                print('NO')
            else:
                print(f'YES {aver - c}')
        elif time < 3:
            print(f'Avg : {aver}')
            if  aver <= d:
                print('NO')
            else  :
                print(f'YES {aver-d}')
high = int(input('hight of electric poles : '))
pole = int(input('number of electric poles : '))
max = 0
max2 = 0
sum = 0
for i in range(pole):
    cost = int(input())
    if cost >= max :
        max2 = max
        max = cost
    elif cost >= max2:
        max2 = cost
    sum = sum + cost
time = max//max2
if time >= 3 :
    sum = sum-max
    aver = int(sum/(pole-1)) + int(max/time)
elif time < 3 :
    aver = int(sum/pole)
if high <=1:
    polehigh(1000,3000)
elif high >1 and high<=4:
    polehigh(5000,10000)
elif high >4 and high<=8:
    polehigh(30000,50000)
else :
    polehigh(75000,100000)'''
#hw2 4
'''d= int(input('d: '))
m =int(input('m: '))
y =int(input('y: '))
day = 0
if m == 1:
    day = d
    print(day)
day = 31
if m == 2 :
    day = day+d
    print(day)
if y%4 == 0 and y%100 != 0:
    day = day+29
else  :
    day = day+28
if m == 3:
    day = day+d
    print(day)
day = day + 31
if m == 4:
    day = day+d
    print(day)
day = day + 30
if m == 5:
    day = day+d
    print(day)
day = day + 31
if m == 6:
    day = day+d
    print(day)
day = day+30
if m == 7:
    day = day+d
    print(day)
day = day +31
if m == 8:
    day = day+d
    print(day)
day = day + 31
if m == 9:
    day = day+d
    print(day)
day = day + 30
if m == 10:
    day = day+d
    print(day)
day = day + 31
if m == 11:
    day = day+d
    print(day)
day = day +30
if m == 12:
    day = day+d
    print(day)
'''
'''#hw2 05
ni,ki = 1,1
n = int(input())
same = n
maxx= n
while n != 0 :
    n = int(input())
    if same == n :
        ni = ni + 1
    elif same != n :
        if  ni > ki :
            ki = ni
            maxx = same
        same = n
        ni = 1
print(ki)
print(maxx)
# hw2 6'''
'''p = int(input())
for i in range(1,p+1) :
    if i%2 == 0 :
        continue
    spac = int((p-i)/2)
    print(' '*spac,'O'*i)'''
# hw2 7
'''p = int(input())
for i in range(1,p+1) :
    if i%2 == 0 :
        continue
    spac = int((p-i)/2)
    print(' '*spac,'O'*i)
for i in range(p-1,0,-1) :
    if i%2 == 0 :
        continue
    spac = int((p-i)/2)
    print(' '*spac,'O'*i)'''
# hw2 8
'''
a = int(input('A: '))
b = int(input('B: '))
c = int(input('C: '))
A = 'A'
B = 'B'
C = 'C'
while True :
    while True :
        if a<b:
            a,b=b,a
            A,B=B,A
        elif b<c:
            b,c = c,b
            B,C = C,B
        else :
            break
    if a==1:
        break
    a = a-1
    b = b-1
    c = c+1
print(C)
'''
x = int(input())
num = x
times = 1
final_times = 1
nummax = x

while x != 0:
  x = int(input())
  if(num == x):
    times = times+1
  else  :
    if(times>final_times):
      final_times = times
      nummax = num
    num = x
    times = 1

print(final_times)
print(nummax)