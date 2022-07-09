import mysql.connector as mysql
import pandas as pd
import matplotlib.pyplot as plt


mydb = mysql.connect(host="localhost", user="root", password="root", port="8889", database="tutor")

cursor = mydb.cursor(dictionary=True) # open sql editor (white page)
cursor.execute("select * from user")

myresult = cursor.fetchall()

#print(myresult)

"""for row in myresult:
 print(row["firstname"])"""
user_df = pd.DataFrame(myresult)
print(user_df)

cursor.close()
mydb.close()


"""plt.bar(user_df["firstname"], user_df["age"])
plt.xlabel("Name")
plt.ylabel("Age")
plt.title("User data")
plt.show()"""



