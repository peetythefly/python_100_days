# The old way
# import csv
# with open(file="weather_data.csv") as weather_file:
#     # weather_lines = weather_file.readlines()
#     weather_data = csv.reader(weather_file)
#     temps = []
#     for row in weather_data:
#         temps.append(row[1])
#     temps.pop(0)
#     print(temps)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
# Working with Columns.
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# average = 0
# for t in temp_list:
#     average += t
# average = average / len(temp_list)
# print(f"Average temperature is {round(average)}")
# print(data["temp"].mean())
# print(data["temp"].max())
# 
# # Two variations but they do the same thing.
# print(data["temp"])
# print(data.temp)

# # Work with rows by adding a conditional as an argument.
# print(data[data.day == "Monday"])
# # Get the row with the max temperature.
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print(monday.condition)
# # Get Monday's temp in F instead of C.
# m_temp = monday.temp[0]
# m_temp_in_f = m_temp * 1.8 + 32
# print(f"Temp in F is {m_temp_in_f}")

# Create a data frame from scratch and not from a csv.
student_dict = {
    "students" : ["Jack", "Jill", "Hansel", "Gretel"],
    "scores" : [90, 95, 75, 20]
}

data = pandas.DataFrame(student_dict)
print(data)
# You can export that dict to a csv.
# data.to_csv("new_csv.csv")