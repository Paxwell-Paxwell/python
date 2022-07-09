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