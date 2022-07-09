import matplotlib.pyplot as plt

x_data = [1, 2, 3, 7, 6]
y_data = [1, 3, 1, 2, 4]
x_data2 = [5, 2, 1, 6, 4]
y_data2 = [1, 2, 5, 2, 4]

plt.scatter(x_data, y_data, label="Data a")
plt.scatter(x_data2, y_data2, marker="x", label="Data b")
plt.title("Scatter graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid()
plt.show()