import matplotlib.pyplot as plt



#data age and speed of 13 cars
x_data = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6, 7] # age of car
y_data = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86, 92] # speed of car
color = [0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100, 55]

fig, axs = plt.subplots(3, 1, figsize=(15,15)) # (row, column, position)
im = axs[2].scatter(x_data, y_data, label="02-06-2022", c=color, cmap="viridis")
axs[2].set_title("Age and speed of 13 cars")
axs[2].set_xlabel("Age")
axs[2].set_ylabel("Speed")
axs[2].legend()
axs[2].grid()
fig.colorbar(im)

#graph 2
x_data = [1, 2, 3, 4, 5]
y_data = [1, 2, 3, 4, 5]
x_data2 = [1, 2, 3, 7, 6]
y_data2 = [1, 3, 1, 2, 4]
x_data3 = [1, 2, 3, 4, 5]
y_data3 = [5, 4, 3, 2, 1]

axs[0].plot(x_data, y_data, marker="o", label="Com")
axs[0].plot(x_data2, y_data2, marker="^", label="Bio")
axs[0].plot(x_data3, y_data3, marker="x", label="Math")
axs[0].set_title("Line graph")
axs[0].set_xlabel("X")
axs[0].set_ylabel("Y")
axs[0].grid(axis="x")
axs[0].legend() # show label of data

#graph 3
#step1: prepare data x and data y (list, tuple, Dataframe)
x_data = ["Com", "Math", "Bio", "Python"]
y_data = [85, 72, 67, 89]

#step2: create graph

axs[1].bar(x_data, y_data, color="#6cf5ce", label="subject term 1")
#plt.barh(x_data, y_data, color="green")

#step3: label your graph
axs[1].set_title("Score data")
axs[1].set_xlabel("Subject")
axs[1].set_ylabel("Score")
axs[1].legend()

#step4: show graph
plt.show()