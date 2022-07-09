code = '''
def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
'''

'''with open('mymodule.py', 'w') as f:
  f.write(code)

##--------------------------------------

import mymodule

with open('mymodule.py') as f:
  print(f.read())

mymodule.greeting('Kun Titi')
a = mymodule.person1["age"]
print(a)'''
'''
my = {1: 11, 2: 8, 3: 7, 4: 6, 5: 12, 6: 6, 7: 9, 8: 11, 9: 8, 10: 12}
data = []
mysort = {}
for i in my.keys():
  data.append(i)
for i in range(len(data)):
  for j in range(i,len(data)-1):
     if my[data[i]]<my[data[j+1]]:
       data[i],data[j+1] = data[j+1], data[i]
for i in data:
  mysort[i] =my[i]
print(mysort)'''
