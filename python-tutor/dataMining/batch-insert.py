import pandas as pd
import mysql.connector as mysql
import datetime

user_df = pd.read_excel("resource/user_data.xlsx")
#print(user_df)
mydb = mysql.connect(host="localhost", user="root", password="root", port="8889", database="tutor")
cursor = mydb.cursor(dictionary=True) # open sql editor (white page)

for index, item in list(user_df.iterrows()):
    firstname = item["firstname"]
    lastname = item["lastname"]
    gender = item["gender"]
    email = item["email"]
    password = item["password"]
    birthdate = item["birthdate"]
    age = datetime.datetime.now().year - int(birthdate.split("-")[0])

    cursor.execute(f"select email from user where email ='{email}'")
    check_email = cursor.fetchall()
    if len(check_email) == 0:
        cursor.execute(f"insert into user(firstname,lastname,gender,email,password,birthdate,age) values('{firstname}',"
                   f"'{lastname}','{gender}','{email}','{password}','{birthdate}',{age})")
        mydb.commit()
        rowcount = cursor.rowcount
        if rowcount == 1:
            print(f'insert {email} success ...')
        else :
            print(f'insert {email} not success ...')
    else:
        print(f'same email:{email}')
cursor.close()
mydb.close()
