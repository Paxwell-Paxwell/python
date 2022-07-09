score_list = (50, 60, 70, 80, 90) # tuple can't insert, remove, edit, sort
print(score_list)

print(score_list[2]) # get data by index
print(score_list[1:4]) # [start:stop+1] get data by range
print(score_list[1:]) # [start:] get data by range to end of list
print(score_list[:3]) # [:stop+1] get data by range from start to stop
print(score_list[::-1]) # invert list

print("///////////////////////////")

#found = score_list.index(200)
#print(found)
foundBoo = 200 in score_list
print(foundBoo)

print("///////////////////////////")

sumValue = sum(score_list)
minValue = min(score_list)
maxValue = max(score_list)
avgValue = sumValue/len(score_list)

print(f"sumValue = {sumValue}")
print(f"minValue = {minValue}")
print(f"maxValue = {maxValue}")
print(f"avgValue = {avgValue}")
print(score_list)

print("///////////////////////////")

for i in range(len(score_list)): # 0-5
    print(score_list[i])

for item in score_list: # for-each
    print(item)