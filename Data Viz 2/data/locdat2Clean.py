import pandas as pd

data = pd.read_csv("https://raw.githubusercontent.com/dnguyen220022/FIT3179/refs/heads/main/Data%20Viz%202/data/locdat2Original.csv", encoding = "latin1")

#drop rows with wrong data
data = data.drop(data[~data["Incident.month"].isin(range(1,13))].index)
print("done")
data["Incident.year"] = pd.to_numeric(data["Incident.year"], errors='coerce')
data["Latitude"] = pd.to_numeric(data["Latitude"], errors='coerce')
data["Longitude"] = pd.to_numeric(data["Longitude"], errors='coerce')
data = data.dropna(subset=["Incident.year", "Latitude", "Longitude"])
print("done")
data = data.drop(data[data["Injury.location"] == "minor lacerations"].index)
print("done")
data = data.drop(data[data["Injury.severity"] == "male"].index)
print("done")
data = data.drop(data[~data["Victim.gender"].isin(["male", "female"])].index)
print("done")
data.to_csv("Data Viz 2\\data\\locdat2.csv", index=False)