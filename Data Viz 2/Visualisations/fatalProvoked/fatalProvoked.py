import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/dnguyen220022/FIT3179/refs/heads/main/Data%20Viz%202/data/locdat2.csv", encoding = "latin1")

data = data[["Shark.common.name", "Provoked.unprovoked", "Victim.injury"]]
data = data.dropna()

shark_counts = data["Shark.common.name"].value_counts()
top_sharks = shark_counts.nlargest(5).index

data["Shark.label"] = data["Shark.common.name"].apply(lambda x: x if x in top_sharks else 'Other')

aggregated_data = data.groupby("Shark.label").agg(
    totalAtt=("Shark.label", "count"),  # Count total attacks per shark type
    unprovokedAttProp=("Provoked.unprovoked", lambda x: (x == "unprovoked").sum() / (x != None).sum() * 100),  # Count provoked attacks
    fatalAttProp=("Victim.injury", lambda x: (x == "fatal").sum() / (x != None).sum() * 100)  # Count fatal attacks
).reset_index()

print(aggregated_data)

aggregated_data.to_csv("Data Viz 2\Visualisations\\fatalProvoked\\fatalProvoked.csv", index=False)