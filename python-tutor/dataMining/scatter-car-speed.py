import matplotlib.pyplot as plt

#data age and speed of 13 cars
x_data = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6, 7] # age of car
y_data = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86, 92] # speed of car
color = [0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100, 55]

plt.scatter(x_data, y_data, label="02-06-2022", c=color, cmap="viridis")
plt.title("Age and speed of 13 cars")
plt.xlabel("Age")
plt.ylabel("Speed")
plt.legend()
plt.grid()
plt.colorbar()
plt.show()