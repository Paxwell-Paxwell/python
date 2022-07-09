def num1():
    total = 0
    for i in data.keys():
        total += data[i]['Total Cases']
    print(total)
def num2():
    max = 0
    for i in data.keys():
        sum = data[i]['Deaths']
        if sum > max:
            max = sum
            cmax = i
    print(cmax)
def num3():
    max = 0
    for i in data.keys():
        sum = data[i]['Total Cases']
        per = data[i]['Deaths']/sum*100
        if per > max:
            max = per
            cmax = i
    print(cmax)
def num4():
    max = 0
    for i in data.keys():
        sum = data[i]['Total Cases']
        per = data[i]['Discharged']/sum*100
        if per > max:
            max = per
            cmax = i
    print(cmax)
def num5():
    total = 0
    for i in data.keys():
        total += data[i]['Total Cases']
    ctotal = 0
    for i in data.keys():
        ctotal += data[i]['Active']
    x = ctotal/total *100
    print(f'{x:.2f}%')
def getkey(dic,i,newdic):
    for k,v in dic.items():
        if v == i:
            if k in newdic.keys():
                continue
            return k
def num6():
    da ={}
    value = [0,0,0,0,0]
    for i in s:
        a = i.strip().split(',')
        x = [int(i) for i in a[5:]]
        da[a[0]] = sum(x)/7
        if da[a[0]] > value[-1]:
            value[-1] = da[a[0]]
        value.sort(reverse=True)
    sort_5value ={}
    for i in value:
        key = getkey(da,i,sort_5value)
        sort_5value[key] = i
    print(sort_5value)
def num7():
    redarea = []
    for i in s:
        a = i.strip().split(',')
        x = [int(i) for i in a[5:-2]]
        for j in range(len(x)):
            if x[j]<100:
                break
        if j == 4:
            redarea.append(a[0])
    redarea.sort()
    for i in redarea:
        print(i)

def cho(num):
    if num ==1:
        num1()
    elif num ==2:
        num2()
    elif num ==3:
        num3()
    elif num == 4:
        num4()
    elif num == 5:
        num5()
    elif num == 6:
        num6()
    elif num == 7:
        num7()
file_name = input('filename: ')
with open(file_name) as f:
    header = f.readline()
    s = f.readlines()
typ = int(input('type: '))
data = {}
for i in s:
    a = i.strip().split(',')
    data[a[0]] = {}
    for j in header.strip().split(',')[1:]:
        data[a[0]][j] = 0
        i = 1
    for t in data[a[0]].keys():
            data[a[0]][t] = int(a[i])
            i += 1
#print(data)
cho(typ)





