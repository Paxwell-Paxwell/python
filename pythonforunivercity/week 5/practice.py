def printGrades(studDic):
    print('\n\n')
    for k, v in studDic.items():
        print(f'\nStudent\'s name: {k}')
        mysum, credit = 0, 0
        for p, q in v.items():
            print(p, ':', q)
            mysum += subDic[p] * grade[q]
            credit += subDic[p]
        gpa = f'{mysum / credit:.2f}'
        print(f' GPA: {gpa}')
    print('Done..')


def printGrades_V2(studDic):
    s = ''
    for k, v in studDic.items():
        s += f'{k}: '  # name
        for p, q in v.items():  # enrolled subject and grade
            s += f'{p} ({subDic[p]}c,{q}), '
        s += f'GPA={str(calGPA(v))}'
        print(s)
        s = ''
    print('DONE GoodBye..')


def calGPA(enrollSub):
    mysum, credit = 0, 0
    for k, v in enrollSub.items():
        mysum += subDic[k] * grade[v]
        credit += subDic[k]
    gpa = f'{mysum / credit:.2f}'
    return gpa