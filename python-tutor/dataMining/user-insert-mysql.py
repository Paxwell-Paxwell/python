import mysql.connector as mysql
import pandas as pd
import datetime


mydb = mysql.connect(host="localhost", user="root", password="root", port="8889", database="tutor")

cursor = mydb.cursor(dictionary=True) # open sql editor (white page)

firstname = input("Enter firstname: ")
lastname = input("Enter lastname: ")
gender = input("Enter gender: ")
email = input("Enter email: ")
password = input("Enter password: ")
birthdate = input("Enter birthdate (yyyy-mm-dd): ")
age = datetime.datetime.now().year - int(birthdate.split("-")[0])

cursor.execute(f"select email from user where email = '{email}'")
user_result = cursor.fetchall()

if len(user_result) == 0: # []
    cursor.execute(f"insert into user(firstname,lastname,gender,email,password,birthdate,age) values('{firstname}','{lastname}','{gender}','{email}','{password}','{birthdate}',{age})")
    mydb.commit()
    rowcount = cursor.rowcount
    if rowcount > 0:
        print("Insert success...!!")
    else:
        print("Error can't insert")
else:
    print("User already exist...!!")


cursor.close()
mydb.close()



