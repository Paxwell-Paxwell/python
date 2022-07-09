import matplotlib.pyplot as plt

#data age and speed of 13 cars
x_data = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6, 7] # age of car
y_data = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86, 92] # speed of car
sizes = [20, 50, 100, 200, 500, 1000, 60, 90, 10, 300, 600, 800, 75, 500]

plt.scatter(x_data, y_data, label="02-06-2022", s=sizes, alpha=0.5)
plt.title("Age and speed of 13 cars")
plt.xlabel("Age")
plt.ylabel("Speed")
plt.legend()
plt.grid()
plt.show()