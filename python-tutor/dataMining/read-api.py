import requests as req
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

#pd.set_option("display.max_columns", None)

resp = req.get("https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all")
covid_data = resp.json()
covid_df = pd.DataFrame(covid_data)
covid_df["txn_date"] = pd.to_datetime(covid_df["txn_date"])
#print(covid_data[0]["new_case"])
print(covid_df)
print(covid_df.columns.to_list())

#convert type of Dataframe
#covid_df = covid_df.astype({"new_case":"object"})
print(covid_df.dtypes)

#data cleaning
print(covid_df.describe())

x = covid_df["txn_date"]
y = covid_df["new_case"]

#fig, axs = plt.subplots(2, 1, figsize=(28,9))
plt.figure(figsize=(16,9))
plt.plot(x, y)
plt.title("Covid 19")
plt.xlabel("date")
plt.ylabel("value")
plt.show()

plt.boxplot(y)
plt.title("Covid 19 (Boxplot)")
plt.xlabel("new case")
plt.grid()
plt.show()

covid_df = covid_df.where(covid_df["new_case"] >= 1000)
covid_df = covid_df.dropna()
print(covid_df)

plt.figure(figsize=(16,9))
plt.plot(covid_df["txn_date"], covid_df["new_case"])
plt.title("Covid 19")
plt.xlabel("date")
plt.ylabel("value")
plt.show()


model = LinearRegression()

x = np.array(covid_df["txn_date"]) # convert list to array
y = np.array(covid_df["new_case"]) # convert list to array
x = x.reshape(-1, 1) # convert x to array 2D

model.fit(x, y) # train model
# step3 check r value
r = model.score(x, y)
print(r)