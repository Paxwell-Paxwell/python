#1
'''def cutbscore(name):
    data[name].sort(reverse=True)
    data[name].remove(data[name][0])
    data[name].remove(data[name][-1])
    data[name] = sum(data[name])
file_name = input('File name: ')
with open(file_name) as f:
    data = {}
    for line in f:
        d = line.strip().split()
        name = d[0]
        data[name] = []
        d.remove(name)
        for i in range(len(d)):
            data[name].append(int(d[i]))
        cutbscore(name)
max = 0
for i in data.values():
    if i > max:
        max = i
print(max)
for i in data.keys():
    if data[i] == max:
        print(i)'''
#2
'''def mul_matrix(A,B) :
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
def plus_matrix(A,B) :
    sumAB = []
    for x in range(len(A)):
        add = []
        for y in range(len(A[0])):
            add.append(A[x][y] + B[x][y])
        sumAB.append(add)
    return sumAB
def print_matrix(res):
    for i in range(len(res)):
        for j in range(len(res[0])):
            print(f"{res[i][j]:^5}", end=" ")
        print()
file_name = input('File name: ')
with open(file_name) as f:
    allmat = []
    mat = []
    ope = []
    s = f.readlines()
    for line in s :
        if line.strip() not in ['+','*']:
            mat.append([int(i) for i in line.strip().split()])
        elif line.strip() in ['+','*',]:
            allmat.append(mat)
            mat = []
            ope.append(line.strip())
        if line == s[-1]:
            allmat.append(mat)
for i in range(len(allmat)):
    if  i == 0:
        total = allmat[0]
    elif i > 0:
        if ope[i-1] == '*':
            total = mul_matrix(total,allmat[i])
        elif ope[i-1] == '+' :
            total = plus_matrix(total,allmat[i])
print_matrix(total)'''
#3
'''def check():
    for line in s:
        data = list(line.split())
        if line in ['Price','List']:
            key = line
            continue
        if key == 'Price':
            if len(data) == 1:
                food_price[data[0]] = 0
            else :
                food_price[data[0]] = int(data[1])
        elif key == 'List':
            if len(data) == 1:
                food_list[data[0]] = 0
            else :
                food_list[data[0]] = int(data[1])
def total():
    total = 0
    for name in food_list.keys():
        if name not in food_price.keys():
            food_price[name] = 0
        total += food_list[name]*food_price[name]
    return total
file_name = input('File name: ').strip()
with open(file_name) as f:
    s = [i.strip() for i in f.readlines()]
    food_price = {}
    food_list = {}
    key = ''
    check()
    for line in s :
        print(line)
    total_price = total()
print(f'Total price: {total_price}')'''
#04
'''
file_name = input('File name: ')
data = {'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
with open(file_name) as f:
    s = f.readlines()
key = ''
for line in s:
    if line.strip() in ['1','2','3','4','5','6','7','8','9']:
        key = line.strip()
        continue
    if line.strip() == '0':
        break
    data[key] += line
w = ''
for i in data.keys():
    w += data[i]
print(w,end='')
'''
#05
'''
def check(height,price):
    if height > 8 and price <= 75000:
        c = 'No'
    elif 4<height<= 8 and price <= 30000:
        c = 'No'
    elif 1<height<= 4 and price <= 5000:
        c = 'No'
    elif height <= 1 and price <= 1000:
        c = 'No'
    else :
        c = 'Yes'
    return c
file_name = input('Filename : ')
data_co = []
with open(file_name) as f:
    header = f.readline()
    s = f.readlines()
    for line in s:
        a = line.strip().split(',')
        No,Height,Cost = int(a[0]),int(a[1]),int(a[2])
        if check(Height,Cost) == 'Yes':
            data_co.append(No)
            data_co.sort()
if len(data_co) == 0:
    print('No')
else:
    print('Yes')
    for i in data_co:
        if i == data_co[-1]:
            print(i,end='')
            break
        print(i)'''
#201
'''def split_n(n):
  #nคือจำนวนที่แตกต่างกันได้เช่นเหมือรทุกตัว n=0
    data = []
    idc = []
    new = ''
    i = 0
    while i < len(text):
        nsame = 0
        w = ''
        if i + len(s) <= len(text):
            for j in range(i, i + len(s)):
                if text[j] != s[j - i]:
                    nsame += 1
                    w += '?'
                else:
                    w += text[j]
        else:
            nsame = 2
        #print(text[i], nsame, )
        if nsame <= n:
            idc.append(i)
            if len(idc) > 1:
                if idc[-1] - len(s) != idc[-2]:
                    if new != '':
                        data.append(new)
            else:
                if new != '':
                    data.append(new)
            if w != '':
                data.append(f'[{w}]')
            if i + len(s) <= len(text):
                i += len(s)
            else:
                i += 1
            new = ''
        elif nsame > n:
            new += text[i]
            i += 1
    if new != '':
        data.append(new)
    #print(data)
    #print(idc)
    return data
text = input('Text: ')
s = input('Substring: ')
if len(split_n(0)) == 1:
    for i in split_n(1):
        print(i,end='')
else :
    for i in split_n(0):
        print(i,end='')'''
#202
'''file_name = input('File name: ')
with open(file_name) as f:
    a= f.read()
    sentense = [i for i in a.split('.') if i != '']
    word = a.split()
    print(f'There are {len(sentense)} sentences and {len(word)} words.')'''
#203
'''def num1():
    print(len(s)+1)
def num2():
    max = 'tvshow'
    for i in data.keys():
        if data[i] > data[max]:
            max = i
    print(max)
def num3():
    blueplanet3 = [0,0,0]
    for i in user.keys():
        if  user[i]['blueplanet']>blueplanet3[2]:
            blueplanet3[2]= user[i]['blueplanet']
        blueplanet3.sort(reverse=True)
    for i in blueplanet3:
        print(i,end=' ')
def num4():
    max = 0
    for i in user.keys():
        sumuser = 0
        for j in user[i].keys():
            sumuser += user[i][j]
        if sumuser > max:
            max = sumuser
            uidmax = i
    print(uidmax,max,end='')
def num5():
    max = 0
    for i in user.keys():
        if user[i]['tvshow'] > max:
            max = user[i]['tvshow']
            uidmax = i
    print(uidmax, max, end='')
def num6():
    c = 0
    for i in user.keys():
        if user[i]['korea'] >500:
             c += 1
    print(c)
def num7():
    c = 0
    for i in user.keys():
        if user[i]['siam']>user[i]['food']:
            c += 1
    print(c)
def num8():
    max = 0
    for i in user.keys():
        sumuser = 0
        for j in user[i].keys():
            sumuser += user[i][j]
        proportion_rajdumnern = user[i]['rajdumnern']/sumuser
        if proportion_rajdumnern > max:
            max =proportion_rajdumnern
            maxuid = i
    print(maxuid)
def num9():
    c = 0
    for i in user.keys():
        percent_data = []
        sumuser = 0
        for j in user[i].keys():
            sumuser += user[i][j]
        for k in user[i].keys():
            percent_data.append(user[i][k]/sumuser *100)
        percent_data.sort(reverse=True)
        plus2room = percent_data[0]+percent_data[1]
        if plus2room > 70:
           c += 1
    print(c)
def num10():
    c = 0
    for i in user.keys():
        if user[i]['pantip'] == 0:
             c += 1
    print(c)
def choice(num):
    if num == 1:
        num1()
    elif num == 2:
        num2()
    elif num == 3:
        num3()
    elif num == 4:
        num4()
    elif num == 5:
        num5()
    elif num == 6:
        num6()
    elif num == 7:
        num7()
    elif num == 8:
        num8()
    elif num == 9:
        num9()
    elif num == 10:
        num10()
file_name = input('File name: ')
num = int(input('enter number: '))
data = {}
user = {}
with open(file_name) as f:
    header = f.readline()
    s = f.readlines()
for i in header.strip().split(','):
    if i != 'uid':
        data[i] = 0
for line in s:
    a = line.strip().split(',')
    j = 0
    user[a[-1]] = {}
    for i in data.keys() :
        data[i] += int(a[j])
        user[a[-1]][i] = int(a[j])
        j += 1
choice(num)'''
#204
'''
def unlock():
    un = []
    for pub in password.keys():
        u = ''
        if 48 <= ord(password[pub][0]) <= 57:
            for i in range(len(pub)):
                k = (ord(pub[i])+ord(password[pub][i]))%26+97
                u += chr(k)
        else:
            for i in range(len(pub)):
                k = (ord(pub[i])+ord(password[pub][i]))%26+65
                u += chr(k)
        un.append(u)
    return un
pub_file = input('Enter publickey filename : ')
pri_file = input('Enter privatekey filename : ')
password = {}
k = {}
with open(pub_file) as f:
    pub = f.readlines()
with open(pri_file) as f:
    pri = f.readlines()
for i in range(len(pub)):
    password[pub[i].strip()] = pri[i].strip()
for i in unlock():
    print(i)
'''
#205
file_name = input('filename: ')
with open(file_name) as f:
    w = [i.lower() for i in f.read().split() if i != '']
computer = 0
for i in w:
    if i.strip('.') in ['computer','computers']:
        computer += 1
print(f'Count = {computer}')



























