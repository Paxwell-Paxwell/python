import mysql.connector as mysql

mydb = mysql.connect(host="localhost", user="root", password="root", port="8889", database="tutor")
cursor = mydb.cursor(dictionary=True) # open sql editor (white page)

name = input("Enter name (for delete): ")
cursor.execute(f"select * from user where firstname = '{name}'")
user_data = cursor.fetchall()

if len(user_data) == 0:
    print("User not found!! Please try again")
else:
    confirm = input("User found.... Delete user(Y/n): ")
    if confirm == "Y":
        cursor.execute(f"delete from user where firstname = '{name}'")
        mydb.commit()
        rowcount = cursor.rowcount

        if rowcount == 0:
            print("Error..!! can't delete data")
        else:
            print(f"Delete success ({rowcount} datas)")

cursor.close()
mydb.close()