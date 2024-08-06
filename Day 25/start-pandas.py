# with open("./weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd
import numpy as np

# data = pd.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# data_list = data["temp"].to_list()
# print(data_list)
#
# num = np.array(data_list)
# average_num = round(np.average(num),2)
# print(average_num)
#
# max_value = data["temp"].max()
# print(max_value)

# print(data[data["day"] == "Monday"])
#
# max_value = data.temp.max()
# print(data[data.temp == max_value])

# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# monday_temp = monday.temp
# temp_fahrenheit = (monday_temp * 9/5) + 32
# print(temp_fahrenheit)

#  Create a dataframe from scratch

# data_dict = {
#
#     "students": ["Amy","James","Angela"],
#     "scores": [76,56,65]
# }
#
# datas = pd.DataFrame(data_dict)
# datas.to_csv("new_data.csv")


data = pd.read_csv("squirrel_data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {

    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]

}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")





