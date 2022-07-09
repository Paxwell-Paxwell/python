'''
word  = input('Enter a string, such as "ILoveYou" : ')
n = len(word)
m = [i for i in word]
matrix = []
for i in range(1,len(m)+1):
    add = []
    for j in range(i):
        add.append(m[j])
    for j in range(i-2,-1,-1):
        add.append(m[j])
    matrix.append(add)
for i in matrix:
    a = ''
    for j in i:
        a += j+" "
    if i != matrix[-1]:
        print(f' {a:^{4*n-3}}')
    else:
        print(f'{a:^{4 * n - 3}}')
matrix.reverse()
for i in matrix:
    if i == matrix[0]:
        continue
    a = ''
    for j in i:
        a += j+" "
    print(f' {a:^{4*n-3}}')'''
'''
word1 = input('Enter a string 1')
word2 = input('Enter a string 2')
word  = input('Enter a string, such as "ILoveYou" : ')
n = len(word)
m = [i for i in word1]
m1= [i for i in word2]
matrix = []
for i in range(1,len(m)+1):
    add = []
    for j in range(i):
        for space in range():
        add.append(m[j])
    for j in range(i-2,-1,-1):
        add.append(m[j])
    matrix.append(add)
'''

'''class student:
    def __int__(self,id1,name1,percentage,id2,name2):
        self.id1 =id1; self.name1 =name1; self.percentage =float(percentage)
        self.id2 =id2; self.name2 = name2
def readStudent(filename):
  mystudent = []
  with open(filename) as fp:
    c = fp.readline()
    for c in fp:
      cc = c.strip().split(',')
      id1,name1,percentage,id2,name2 = cc[0], cc[1], cc[2], cc[3],cc[4]
      mystudent.append(student(id1,name1,percentage,id2,name2))
  return mystudent
filename = input('Enter your Filename: ')
mystudent = readStudent(filename)
naorid = input('Show by name or id?: ')
percen = int(input('How many similarity percentages do you want?: '))
filstudent = []
for i in mystudent:
    if i.percentage > 70:
        filstudent.append(i)
gro = []
for i in filstudent:
    a = false
    for j in gro:
        if
        elif i.name1 in samestudent or i.name2 in samestudent:
            if i.name1 not in samestudent:
                samestudent.append(i.name1)
            elif i.name2 not in samestudent:
                samestudent.append(i.name2)
    gro.append(samestudent)'''

# ID(1) 0,Name(1) 1,Percentage 2,ID(2) 3,Name(2) 4
file = input("Enter your Filename: ")
data = []
with open(file, "r") as fp:
    fp.readline()
    for d in fp:
        d = d.strip().split(",")
        data.append(d)
case = input("Show by name or id?: ")
percent = float(input("How many similarity percentages do you want?: "))
group = {}
top = {}
i = 1
for d in data:
    if float(d[2]) >= percent:
        if case == "name":
            p1 = d[1]
            p2 = d[4]
        else:
            p1 = d[0]
            p2 = d[3]
        flag = False
        for g in group:
            if p1 in group[g] and p2 in group[g]:
                top[p1] += 1
                top[p2] += 1
                flag = True
                break
            elif p1 in group[g]:
                group[g].append(p2)
                top[p1] += 1
                top[p2] = 1
                flag = True
                break
            elif p2 in group[g]:
                group[g].append(p1)
                top[p1] = 1
                top[p2] += 1
                flag = True
                break
        if not flag:
            group[i] = [p1, p2]
            top[p1] = 1
            top[p2] = 1
            i += 1
print("==============================")
for g in group:
    msg = " ".join(sorted(set(group[g])))
    print(f"Group{g}: {msg}")
print("==============================")
tops = int(input("Input number of top similarity: "))

last = None
top = sorted(top.items(), key=lambda item: item[1], reverse=True)
temp = {}
for t in top:
    if t[1] in temp:
        temp[t[1]].append(t[0])
    else:
        temp[t[1]] = [t[0]]
for t in temp:
    temp[t] = sorted(temp[t])
for t in temp:
    for i in temp[t]:
        print(i)
        tops -= 1
        if tops == 0:
            break
    if tops == 0:
        break