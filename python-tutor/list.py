#test2
score_list = [50, 60, 70, 80, 90]
print(score_list)

print(score_list[2]) # get data by index
print(score_list[1:4]) # [start:stop+1] get data by range
print(score_list[1:]) # [start:] get data by range to end of list
print(score_list[:3]) # [:stop+1] get data by range from start to stop
print(score_list[::-1]) # invert list

print("///////////////////////////")

score_list[2] = 99 # edit data by index
score_list.append(199) # add data to end of list
score_list.insert(0, 10) # add data by index
print(score_list)

score_list.remove(60) # remove by data
print(score_list)

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
#score_list.sort() # asc
score_list.sort(reverse=True) # desc

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









