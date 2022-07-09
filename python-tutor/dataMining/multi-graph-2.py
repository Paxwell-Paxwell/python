import matplotlib.pyplot as plt

#step1: prepare data x and data y (list, tuple, Dataframe)
x_data = ["Com", "Math", "Bio", "Python"]
y_data = [85, 72, 67, 89]

#step2: create graph
plt.bar(x_data, y_data, color="#6cf5ce", label="subject term 1")
#plt.barh(x_data, y_data, color="green")

#step3: label your graph
plt.title("Score data")
plt.xlabel("Subject")
plt.ylabel("Score")
plt.legend()

#step4: show graph
plt.show()


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