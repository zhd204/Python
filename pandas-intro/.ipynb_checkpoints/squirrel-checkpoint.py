import numpy as np
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_set = set(data['Primary Fur Color'])
color_set.remove(np.nan)
color_dict = {"Fur Color": [], "Count": []}
for color in color_set:
    fur_color_group = data.groupby(data["Primary Fur Color"] == color).count()["Primary Fur Color"]
    color_dict["Fur Color"].append(color)
    color_dict["Count"].append(fur_color_group.loc[True])

print(color_dict)
pd_data = pandas.DataFrame(color_dict)
print(pd_data)

pd_data.to_csv('squirrel_count.csv')



