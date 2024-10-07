import pandas as pd

data = pd.read_csv("locdat2Original.csv")

#drop rows with wrong data
data = data.drop(data[~data["Incident.month"].isin(range(1,13))].index)
data = data.drop(data[~data["Incident.year"].apply(lambda x: isinstance(x, int))].index)
data = data.drop(data[~data["Latitude"].apply(lambda x: isinstance(x, float))].index)
data = data.drop(data[~data["Longitude"].apply(lambda x: isinstance(x, float))].index)
data = data.drop(data[data["Injury.location"] == "minor lacerations"].index)
data = data.drop(data[data["Injury.severity"] == "male"].index)
data = data.drop(data[data["Injury.severity"] == "male"].index)
data = data.drop(data[~data["Victim.gender"].isin(["male", "female"])].index)