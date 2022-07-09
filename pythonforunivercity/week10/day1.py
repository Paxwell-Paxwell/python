
#1
'''import json
file_name =input('Filename : ')
name = input('Data : ')
with open(file_name) as f:
    data = json.loads(f.read())
for i in data:
    b = False
    if i['name'] == name or i['ID number'] == name:
        b = True
        break
if b:
    print('Found in blacklist')
    for k,v in i.items():
        print(f'{k} : {v}')
else:
    print('Not found in blacklist')'''
#2
'''def choice(case):
    sort_id = []
    if case == '0':
        for i in character:
            for y in data.values():
                if y['id'] == int(i):
                    sort_id.append(y['id'])
                    break
        sort_id.sort()
        for i in sort_id:
            for y in data.values():
                if y['id'] == i:
                    print(f'{y["id"]}\t---\t{y["name"]}\t---\t{y["title"]}')
    elif case == '1':
        for i in character:
            for y in data.values():
                if y['name'][0].lower() == i.lower():
                    sort_id.append(y['id'])
        sort_id.sort()
        for i in sort_id:
            for y in data.values():
                if y['id'] == i and i == sort_id[-1]:
                    print(f'{y["id"]}\t---\t{y["name"]}\t---\t{y["title"]}', end='')
                elif y['id'] == i:
                    print(f'{y["id"]}\t---\t{y["name"]}\t---\t{y["title"]}')
    elif case == '2':
        for i in character:
            for y in data.values():
                if y['title'][0:3] in ['the','The']:
                    a = y['title'][4]
                else:
                    a = y['title'][0]
                if a.lower() == i.lower():
                    sort_id.append(y['id'])
        sort_id.sort()
        for i in sort_id:
            for y in data.values():
                if y['id'] == i and i == sort_id[-1]:
                    print(f'{y["id"]}\t---\t{y["name"]}\t---\t{y["title"]}',end = '')
                elif y['id'] == i:
                    print(f'{y["id"]}\t---\t{y["name"]}\t---\t{y["title"]}')

import json
file_name =input('Filename : ')
case = input('Case : ')
character = input('Character : ').split(',')
with open(file_name) as f:
    data = json.loads(f.read())
choice(case)'''
#3
'''import json
file_name =input('Filename : ')
x = input()
with open(file_name) as f:
    data = json.loads(f.read())
    obj = {}
for i in data:
    if i['Product type'] == x:
        obj[i['Brand']] = int(i['Cost'])
i = 0
for k,v in obj.items():
    if i == 0:
        min = v
    if min >= v:
        min = v
        bmin = k
    i += 1
print(f'{bmin} : {min}')
'''
#4
'''def change(price):
    if price == 0:
        print('no change')
    else:
        total = price
        for i in [1000,500,100,50,20,10,5,2,1]:
            if total//i > 0:
               print(f'{i} : {total//i}')
            total = total%i
import json
file_name =input('Enter json filename : ')
with open(file_name) as f :
    data = json.loads(f.read())
newdata = []
newdatadic ={}
for i in data['customers']:
    m = 0
    for k,v in i['order'].items():
        for j in data['products']:
            if j["product_name"] == k:
                price = int(j["price"])
                break
        m += price*v
    change_money = i["money"]-m
    newdata.append(i['customer_name'])
    newdatadic[i['customer_name']] = change_money
newdata.sort()
for i in newdata:
    print(i)
    change(newdatadic[i])
    print()'''
#05
'''
import json
file_name =input('Filename : ')
typ = input('type : ')
with open(file_name) as f :
    data = json.loads(f.read())
newdata = {}
for i in data:
    if i["species"] not in newdata.keys():
        newdata[i["species"]] = []
    newdata[i["species"]].append(i[typ])
for k,v in newdata.items():
    print(f'{k} = {sum(v)/len(v):.2f}')
#06
'''
'''
code = \'''
def greeting(name):
  print("Hello, " + name)\'''

with open('mymodule.py', 'w') as f:
  f.write(code)
import mymodule
name = input('Name : ')
mymodule.greeting(name)
'''
#07
'''
code = \'''
def showO(num):
  s = ''
  for i in range(1,num-1):
    if i%2 == 1:
      s += f'{"O"*i:^{num}}'*num+'\\n'
  s += f'{num*"O"}'*num+'\\n'
  for i in range(num-2,1,-1):
    if i % 2 == 1:
      s += f'{"O" * i:^{num}}'*num+'\\n'
  s += f'{"O":^{num}}'*num
  for i in range(1,num+1):
    print(s)\'''
with open('printO.py', 'w') as f:
  f.write(code)
import printO
num = int(input())
printO.showO(num)
'''
'''
def num1():
    people = len(data)
    print(people)
def num2():
    id = {}
    for i in data:
        if i["author"] not in id.keys():
            id[i["author"]] = 1
        else:
            id[i["author"]] += 1
    print(len(id))
def num3():
    max = 0
    id = {}
    user_tweet_max =[]
    for i in data:
        if i["author"] not in id.keys():
            id[i["author"]] = 1
        else:
            id[i["author"]] += 1
    for v in id.values():
        if v > max:
            max = v
    for k,v in id.items():
        if v == max:
            user_tweet_max.append(k)
    for i in user_tweet_max:
        print(i)
def num4():
    topic = {}
    for i in data:
        if i["topic"] not in topic.keys():
            topic[i["topic"]] = 1
        else:
            topic[i["topic"]] += 1
    print(len(topic))
def num5():
    ALERT = 0
    for i in data:
        if i['topic_priority'] == 'ALERT':
            ALERT += 1
    print(ALERT)
def num6():
    UNIMPORTANT = 0
    for i in data:
        if i['topic_priority'] == 'UNIMPORTANT':
            UNIMPORTANT+= 1
    print(UNIMPORTANT)
def num7():
    la = False
    for i in data:
        if i['language'] != "EN":
            la = True
            break
    print(la)
def num8():
    max_word_count = 0
    for i in data:
        word_count = len(i['text'].strip().split())
        if word_count > max_word_count:
            max_word_count = word_count
    print(max_word_count)
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
import json
file_name =input('File name: ')
num = int(input('input: '))
with open(file_name) as f :
    data = json.loads(f.read())
choose(num)'''
#22
'''
def num1():
    print(len(data))
def num2():
    population = 0
    for i in data:
        population += int(i["population"])
    print(population)
def num3():
    first_letter_c = 0
    countryname_more5 = 0
    for i in data:
        if i['country'][0] == 'C':
            first_letter_c += 1
        if len(i['country']) > 5:
            countryname_more5 += 1
    print(first_letter_c)
    print(countryname_more5)
def num4():
    peoplemore500 = 0
    peoplebetween250to750 = 0
    peoplelessthan10 =0
    for i in data :
        if int(i['population']) >500000000:
            peoplemore500 += 1
        if int(i['population'])<=750000000 and int(i['population'])>=250000000:
            peoplebetween250to750 +=1
        elif int(i['population']) <= 10000000:
            peoplelessthan10 += 1
    print(peoplemore500)
    print(peoplebetween250to750)
    print(peoplelessthan10)
def num5():
    percent20firstrank = 0
    percent_between150_50 = 0
    for i in data :
        if 1<=int(i['Rank'])<=20:
            percent20firstrank += float(i['World'])*100
        elif 150>=int(i['Rank'])>=50:
            percent_between150_50 += float(i['World'])*100
    print(f'{percent20firstrank:.2f}')
    print(f'{percent_between150_50:.2f}')
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
import json
file_name =input('File Name: ')
num = int(input('Input : '))
with open(file_name) as f :
    data = json.loads(f.read())
choose(num)
'''
'''
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
def num1():
    print(len(data))
def num2():
    reviewerID = {}
    for i in data:
        if i['reviewerID'] not in reviewerID.keys():
            reviewerID[i['reviewerID']] =1
        else:
            reviewerID[i['reviewerID']] +=1
    print(len(reviewerID))
def num3():
    productID = {}
    for i in data:
        if i['productID'] not in productID.keys():
            productID[i['productID']] = 1
        else:
            productID[i['productID']] += 1
    print(len(productID))
def num4():
    category = {}
    for i in data:
        maincategory = i['category'].split('>')[0].strip()
        if maincategory not in category.keys():
            category[maincategory] = 1
        else:
            category[maincategory] += 1
    print(len(category))
def num5():
    category = {}
    for i in data:
        maincategory = i['category'].split('>')[1].strip()
        if maincategory not in category.keys():
            category[maincategory] = 1
        else:
            category[maincategory] += 1
    print(len(category))
def num6():
    reviewerID = {}
    for i in data:
        if i['reviewerID'] not in reviewerID.keys():
            reviewerID[i['reviewerID']] = 1
        else:
            reviewerID[i['reviewerID']] += 1
    max = 0
    for k,v in reviewerID.items():
        if v > max :
            idmax = k
            max = v
    print(idmax)
def num7():
    productreview = {}
    for i in data:
        a = i['productName']
        if a not in productreview.keys():
            productreview[a] = {}
            productreview[a]['review'] = 1
            productreview[a]['overall'] = [i['overall']]
        else:
            productreview[a]['review'] += 1
            productreview[a]['overall'].append(i['overall'])
    max = 0
    for k,v in productreview.items():
        aver = sum(v['overall'])/len(v['overall'])
        if aver > max:
            max = aver
            rc = v['review']
            bestreview = k
        elif aver == max and v['review'] > rc :
            bestreview = k
            rc = v['review']
    print(bestreview)
def num8():
    p = {}
    for i in data:
        productName = i['productName']
        word_count = len(i['reviewText'].split())
        if productName not in p.keys():
            p[productName] = [word_count]
        else :
            p[productName].append(word_count)
    print(p)
    max =0
    for k,v in p.items():
        aver = sum(v)/len(v)
        if aver >max :
            max =aver
            nproductmax = k
    print(nproductmax)
import json
file_name =input('file name: ')
num = int(input('input: '))
with open(file_name) as f :
    s = f.readlines()
data = []
for i in s:
    data.append(json.loads(i))
choose(num)'''
orders = {
	'cappuccino': 54,
	'latte': 56,
	'espresso': 72,
	'americano': 48,
	'cortado': 41
}

sort_orders = dict(sorted(orders.items(), key=lambda x: x[1]))
print(sort_orders)