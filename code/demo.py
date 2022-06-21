import pandas as pd
titanic = pd.read_csv("train.csv")
print(titanic.head(5))
print(titanic.describe())

# 数据预处理
# 填充缺失值（使用平均值）
# titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())
# # string型转int型
# print(titanic["Sex"].unique())
# titanic["Sex"].loc[titanic["Sex"] == "male", "Sex"] = 0
# titanic["Sex"].loc[titanic["Sex"] == "female", "Sex"] = 1