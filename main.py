import pandas as pd
df = pd.read_csv("data/Students.csv")
print(df.columns.tolist())
# # print(df.head(3))
# # print(df.tail(3))
# print(df["Name"])
# print(df["Python"])
df["Total"] = df["Python"] + df["Java"] + df["DSA"]
print(df)


# # head, columns
