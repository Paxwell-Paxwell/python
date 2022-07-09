import matplotlib.pyplot as plt

def removeOutline(data_list, min, max):
        data_list = list(filter(lambda x: x >= min and x <= max, data_list))
        return data_list
#data age and speed of 13 cars
x_data = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6, 7] # age of car
y_data = [20, 30, 99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86, 92] # speed of car

plt.boxplot(y_data)
plt.title("Age and speed of 13 cars")
plt.xlabel("Speed")
plt.grid()
plt.show()

y_data = removeOutline(y_data, 77, 103)
print(y_data)

plt.boxplot(y_data)
plt.title("Age and speed of 13 cars (remove outline)")
plt.xlabel("Speed")
plt.grid()
plt.show()

