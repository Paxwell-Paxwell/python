import pandas as pd

score_df = pd.read_excel("resource/test-score.xlsx")
#data frame
print(score_df)

for index, item in list(score_df.iterrows()):
    print(item["Score"])
    score = item["Score"]
    grade = "F"
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    elif score < 50:
        grade = "F"
    else:
        print("Score invalid")

    score_df.at[index, "Grade"] = grade

print(score_df)
print(score_df.describe())

score_df.to_excel("resource/final-score.xlsx", sheet_name="Math", index=False)


