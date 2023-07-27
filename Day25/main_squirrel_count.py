#main_squirrel_count
import pandas as pd

data = pd.read_csv("E:/CODING/GitHub Repositories/100-Days-of-Code/Day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
black_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_count, cinnamon_count, black_count]
}

df = pd.DataFrame(data_dict)
df.to_csv("E:/CODING/GitHub Repositories/100-Days-of-Code/Day25/Squirrel_count.csv")