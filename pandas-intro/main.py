# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     next(data)
#     for row in data:
#         temperatures.append(int(row[1]))
#
#     print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(f"Type of data is: {type(data)}")
print(data)
# print(f"Type of data[temp] is: {type(data['temp'])}")
# print(data["temp"])
#
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
# print(data['temp'].index)
# print(data['temp'].shape)
# ave = round(sum(temp_list) / len(temp_list), 2)
# ave = round(data['temp'].mean(), 2)
# print(f"Average temperature is: {ave} degree.")
# max_value = data['temp'].max()
# print(f"Max temperature is: {max_value} degree.")
#
# print(type(data["condition"]))
# print(data["condition"])
# print(type(data.condition))
# print(data.condition)

# Get data in row
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

temp_F = data[data.day == "Monday"].temp * 1.8 + 32

print(temp_F)

# Create a dataframe from scratch
data_dict = {
    "student": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("new_data.csv")