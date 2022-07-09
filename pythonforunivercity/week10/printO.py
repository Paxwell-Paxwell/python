
def showO(num):
  s = ''
  for i in range(1,num-1):
    if i%2 == 1:
      s += f'{"O"*i:^{num}}'*num+'\n'
  s += f'{num*"O"}'*num+'\n'
  for i in range(num-2,1,-1):
    if i % 2 == 1:
      s += f'{"O" * i:^{num}}'*num+'\n'
  s += f'{"O":^{num}}'*num
  for i in range(1,num+1):
    print(s)