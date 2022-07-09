import json
def num1():
    print(len(data))
def num2():
    x = int(input('From : '))
    y = int(input('To : '))
    startchar = input('Start with Char : ')
    newdata = []
    for i in range(x,y+1):
        if data[i]['title'][0].upper() == startchar.upper():
            newdata.append(i)
    for j in newdata:
        print(f'{j} : {data[j]["title"]}')
def num3():
    x = int(input('From : '))
    y = int(input('To : '))
    ty = input('Type : ')
    total = 0
    maxs = 0
    maxf = 0
    for i in range(x,y+1):
        if data[i]['type'] == ty:
            total += 1
            if data[i]['mal_score'] in ['None','Null']:
                data[i]['mal_score'] =0
            if maxs < data[i]['mal_score']:
                maxs = data[i]['mal_score']
                ns = data[i]['title']
            if data[i]['mal_favorites'] in ['None','Null']:
                data[i]['mal_favorites'] = 0
            if maxf < data[i]['mal_favorites']:
                maxf = data[i]['mal_favorites']
                nf = data[i]['title']
    print(f'{ty} : {total}')
    print(f'Most scores : {ns}')
    print(f'Most favorites : {nf}')
def num4():
    x = int(input('From : '))
    y = int(input('To : '))
    sou = input('Source : ')
    sta = input('Status : ')
    mulscore = int(input('Mul score : '))
    newdata = []
    for i in range(x, y + 1):
        if data[i]['source']== sou and data[i]['status'] == sta and data[i]['mal_score'] >= mulscore:
            newdata.append(i)
    for j in newdata:
        print(f'{j} : {data[j]["title"]}')
def num5():
    x = int(input('From : '))
    y = int(input('To : '))
    sea = input('Season : ')
    total = 0
    for i in range(x,y+1):
        if data[i]['premiered'] != None :
            if sea in data[i]['premiered'] :
                total += 1
    print(f'{sea} : {total}')
def num6():
    x = int(input('From : '))
    y = int(input('To : '))
    total = 0
    for i in range(x,y+1):
        if (data[i]['aired_start'] != None) and (data[i]['aired_end'] != None) :
            if data[i]['aired_start'][0:4] == data[i]['aired_end'][0:4]:
                total += 1
    print(f'Find : {total}')
def num7():
    ti = input('Title : ')
    for i in data:
        if i['title'] == ti:
            print(i['mal_rating'])
            break
def num8():
    x = int(input('From : '))
    y = int(input('To : '))
    mw = 0

    for i in range(x,y+1):
        w = len(data[i]['synopsis'].split())
        if w > mw:
            mw = w
            nmw = data[i]['title']
            pomw = i
    print(f'{pomw} : {nmw}')
def choose(num):
    if num == 1:
        num1()
    elif num == 2:
        num2()
    elif num == 3:
        num3()
    elif num ==4:
        num4()
    elif num == 5:
        num5()
    elif num == 6:
        num6()
    elif num ==7:
        num7()
    elif num == 8:
        num8()
filename = input('Filename : ')
menu = int(input('Menu : '))
with open(filename.strip()) as f:
    data = json.loads(f.read())
choose(menu)
