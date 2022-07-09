import matplotlib.pyplot as plt

x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]
x_data2 = [1, 2, 3, 7, 6]
y_data2 = [1, 3, 1, 2, 4]
x_data3 = [1, 2, 3, 4, 5]
y_data3 = [5, 4, 3, 2, 1]

plt.plot(x_data, y_data, marker="o", label="Com")
plt.plot(x_data2, y_data2, marker="^", label="Bio")
plt.plot(x_data3, y_data3, marker="x", label="Math")
plt.title("Line graph")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(axis="x")
plt.legend() # show label of data
plt.show()