'''d = {'a1': 3, 'g5': 3, 'ca':3}
def getkey(dic,i,newdic):
    for k,v in dic.items():
        if v == i:
            if k in newdic.keys():
                continue
            return k
sort = {}
for i in d.values():
    key = getkey(d,i,sort)
    sort[key] = i
print(sort)'''
a = 'sdfgs


