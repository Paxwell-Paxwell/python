def editInt(value): # pass by value
    value = value * 3

def editList(data_list): # pass by reference
    data_list[0] = 999

#main
x = 20
data = [89, 4, 6, 16, 22, 77]

editInt(x)
print(x)

editList(data)
print(data)



