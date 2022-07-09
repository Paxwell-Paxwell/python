import mysql.connector as mysql
import datetime

mydb = mysql.connect(host="localhost", user="root", password="root", port="8889", database="tutor")
cursor = mydb.cursor(dictionary=True) # open sql editor (white page)

name = input("Enter name (for update): ")
cursor.execute(f"select * from user where firstname = '{name}'")
user_data = cursor.fetchall()

if len(user_data) == 0:
    print("User not found!! Please try again")
else:
    confirm = input("User found.... Update user(Y/n): ")
    if confirm == "Y":
        print("Enter data for update...!!\n")
        firstname = input("Enter Firstname: ")
        lastname = input("Enter Lastname: ")
        gender = input("Enter Gender: ")
        email = input("Enter Email: ")
        password = input("Enter Password: ")
        birthdate = input("Enter Birthdate (yyyy-mm-dd): ") # 1994-04-05
        age = datetime.datetime.now().year - int(birthdate.split("-")[0])

        sql = f"update user set "
        if firstname != '':
            sql += f"firstname = '{firstname}' ,"
        if lastname != '':
            sql += f"lastname = '{lastname}' , "
        if gender != '':
            sql += f"gender = '{gender}' , "
        if email != '':
            sql += f"email = '{email}' , "
        if password != '':
            sql += f"password = '{password}' ,"
        if birthdate != '':
            sql += f"birthdate ='{birthdate}' , "
        if age != '':
            sql += f"age = '{age}' "
        sql += f"where firstname = '{name}'"
        #print(sql)
        cursor.execute(sql)
        mydb.commit()
        rowcount = cursor.rowcount

        if rowcount == 0:
            print("Error can't update user")
        else:
            print(f"Update success ({rowcount} datas)")