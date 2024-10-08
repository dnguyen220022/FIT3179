import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/dnguyen220022/FIT3179/refs/heads/main/Data%20Viz%202/data/locdat2.csv", encoding = "latin1")

data = data[["Victim.age"]]
data = data.dropna()

print(data.head())

data.to_csv("Data Viz 2\Visualisations\\attackByAge\\attackbyAge.csv", index=False)