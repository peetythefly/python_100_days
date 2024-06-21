import pandas
from collections import Counter

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240525.csv")

# Find out the count of each color of squirrel. My way
color_counts = Counter()
for color in squirrel_data["Primary Fur Color"]:
    color_counts[color] += 1

common_colors = color_counts.most_common(3)
print (common_colors)
print(f'''There are: 
      {color_counts["Gray"]} Gray squirrels, 
      {color_counts["Cinnamon"]} Cinnamon squirrels, 
      and {color_counts["Black"]} Black squirrels.''')
framed_count = pandas.DataFrame(common_colors)

framed_count.to_csv("squirrel_colors.csv")

# Now we do it Angela's way.
grey_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Red", "Black"],
    "Count": [grey_count, red_count, black_count]
}
angela_framed = pandas.DataFrame(data_dict)
angela_framed.to_csv("angela_colors.csv")