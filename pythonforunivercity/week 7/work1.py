## main begins here
subDic = {'Physic I': 3, 'Lab Physic I': 1, 'Math I': 3, 'Com Programming': 3, 'Thai Lang Com': 3, 'Art of Living': 3, 'Land of Smile': 3, 'Intro Japanese': 3}
subList = ['Physic I', 'Lab Physic I', 'Math I', 'Com Programming', 'Thai Lang Com', 'Art of Living', 'Land of Smile', 'Intro Japanese']
grade = {'A':4,'B+':3.5,'B':3,'C+':2.5,'C':2,'D+':1.5,'D':1,'F':0}
studDic = {'Kun Toto': {'Physic I': 'A', 'Lab Physic I': 'C+', 'Thai Lang Com': 'B+', 'Land of Smile': 'D', 'Intro Japanese': 'B+'},
           'Somchai Rukdee': {'Lab Physic I': 'B+', 'Physic I': 'B', 'Math I': 'C', 'Com Programming': 'D', 'Thai Lang Com': 'F', 'Art of Living': 'A', 'Land of Smile': 'A'}}
def calGrade(v):
    lenV,C,myS = len(v),0,0
    for s, g in v.items():
        C += subDic[s]
        myS += subDic[s]*grade[g]
        print(f'{s} ({subDic[s]},{g})', end=' ')
        lenV -= 1
        if lenV == 0:
            print()
        else:
            print('\', ', end='')
    gpa = f'{myS/C:.2f}'
    print(f' GPA: {gpa}')
def printGrades(studDic):
    for name,v in studDic.items():
        print(f'Name: {name}')
        calGrade(v)
def printSubjMenu():
    lenSubList, s, ss = len(subList), [], ''
    for i in range(lenSubList):
        # print(f'[{i+1}] {subList[i]}')
        ss = f'[{i + 1}] {subList[i]} ({subDic[subList[i]]})'
        s.append(f'{ss:<24}')
        if len(s) % 4 == 0:
            for i in range(len(s)):
                print(s[i], end='')
            print()
            s = []
    if len(s) > 0:
        for i in range(len(s)):
            print(s[i], end='')
def getSubjGrade():
    subGrade = {}
    while True:
        printSubjMenu()
        try:
            n = int(input('Select either subject [1]..[8] or 0: '))
            if n == 0:
                break
            if n not in range(1, 9):
                raise ValueError(f'{n} is NOT 1..8')
        except ValueError as e:
            # print(f'--> e is {e}')
            print(f' ERROR: only either integer 1..8 accepted!')
            continue
        print(f'You select [{subList[n - 1]}]')
        g = input(f'Enter grade you get for {[subList[n - 1]]}: ').upper()
        if g not in grade.keys():
            print(f' ERRORL either of A,B+,B,..,F is accepted!')
            continue
        subGrade[subList[n - 1]] = g
        print(subGrade)
    return subGrade
def myMain():
    studDic = {}
    while True:
      name = input('Enter student\'s name or press ENTER to end: ')
      if name == '':
        printGrades(studDic)
        break
      subjGrade = getSubjGrade()
      print(name, subjGrade)
      studDic[name] = subjGrade
    print(studDic)
with open('studentDic.txt','w') as fp:
    for n,v in studDic.items():
        fp.write(f'{n}')
        for s,g in v.items():
            fp.write(f',{s},{g}')
        fp.write('\n')
stdDico ={}
with open('studentDic.txt','r') as fp:
    for line in fp:
        print(line)
