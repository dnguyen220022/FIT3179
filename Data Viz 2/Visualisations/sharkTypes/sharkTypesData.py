import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/dnguyen220022/FIT3179/refs/heads/main/Data%20Viz%202/data/locdat2.csv", encoding = "latin1")

data = data[["Shark.common.name", "Provoked.unprovoked"]]
data = data.dropna()

shark_counts = data["Shark.common.name"].value_counts()
top_sharks = shark_counts.nlargest(5).index

data["Shark.label"] = data["Shark.common.name"].apply(lambda x: x if x in top_sharks else 'Other')

print(data.head())

data.to_csv("Data Viz 2\Visualisations\sharkTypes\sharkTypes.csv", index=False)