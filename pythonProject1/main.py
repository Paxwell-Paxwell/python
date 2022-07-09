ac = int(input("input"))
walk = input()
action = ''
di = ['e','s','w','n']
for i in walk:
    if len(action) == 0:
        action += i
        continue
    if action == "L":
        action += i
    
    if i == 'F' :

