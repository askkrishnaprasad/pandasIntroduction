# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data = pandas.read_csv("squirrel_count.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
new_data = pandas.DataFrame(data_dict)
new_data.to_csv("data_subset.csv")

# # convert data to a dictionary
# data_dict = data.to_dict()
#
# # convert temperatures to a list of values
# temp_list = data["temp"].to_list()
#
# # find average temperature from list
# # temp_avg = sum(temp_list) / len(temp_list)
# # print(temp_avg)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Two ways to get the columns
# print(data["temp"])
# print(data.temp)
#
# # Way to get the row
# monday = data[data.day == "Monday"]
# print((int(monday.temp)*1.8)+32)
# print(data[data.temp == data.temp.max()])
#
# # create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "Krish", "Ashok"],
#     "scores": [77, 100, 99]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
