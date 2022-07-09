import requests as req
import pandas as pd
import mysql.connector as mysql
resp = req.get("https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all")
covid_data = resp.json()
covid_df = pd.DataFrame(covid_data)
mydb = mysql.connect(host="localhost", user="root", password="root", port="8889", database="tutor")
cursor = mydb.cursor(dictionary=True)

for index, item in list(covid_df.iterrows()):
    txn_date = item["txn_date"]
    new_case = item["new_case"]
    total_case =item["total_case"]
    new_case_excludeabroad = item["new_case_excludeabroad"]
    total_case_excludeabroad = item["total_case_excludeabroad"]
    new_death = item["new_death"]
    total_death = item["total_death"]
    new_recovered = item["new_recovered"]
    total_recovered = item["total_recovered"]
    update_date = item["update_date"]
    cursor.execute(f"select txn_date from covid19 where txn_date = '{txn_date}'")
    ch_txn_date = cursor.fetchall()

    if len(ch_txn_date) == 0:
        sql = f"insert into covid19(txn_date,new_case,total_case,new_case_excludeabroad,total_case_excludeabroad,new_death," \
                f"total_death,new_recovered,total_recovered,update_date) " \
                f"values('{txn_date}', {new_case},{total_case},{new_case_excludeabroad}, " \
                f"{total_case_excludeabroad},{new_death},{total_death},{new_recovered}," \
                f"{total_recovered},'{update_date}')"
        cursor.execute(sql)
        mydb.commit()
        rowcount = cursor.rowcount
        if rowcount == 1:
            print(f'insert {txn_date} success ...')
    else:
        print(f'same txn_date:{txn_date}')
cursor.close()
mydb.close()



