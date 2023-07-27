"""
with open("E:/CODING/GitHub Repositories/100-Days-of-Code/Day25/weather-data.csv") as data_file:
    data = data_file.readlines()
    print(data)
"""

#using csv

import csv


with open("E:/CODING/GitHub Repositories/100-Days-of-Code/Day25/weather-data.csv") as data_file:
    data = csv.reader(data_file)
    for row in data:
        print(row)

#this gives the result in a proper order with each item seperated in a list individually

lst = []
with open("E:/CODING/GitHub Repositories/100-Days-of-Code/Day25/weather-data.csv") as data_file:
    next(data_file)
    data = csv.reader(data_file)
    for row in data:
        a = row[1]
        a = int(a)
        lst.append(a)

print(lst)


#pandas library is useful in such cases to perform data analysis on tabular data

import pandas as pd

data = pd.read_csv("E:/CODING/GitHub Repositories/100-Days-of-Code/Day25/weather-data.csv")
print(data)

print(" ")

#to print column
print(data["temp"])

#to check data type of data we are getting back from pandas
print(type(data))

#to convert into dictionary
data_dict = data.to_dict()
print(data_dict)

#to convert to list
temp_list = data["temp"].to_list()
print(temp_list)


avg_temp = data["temp"].mean()
print(f"Average temperature is: {avg_temp}")

max_temp = data["temp"].max()
print(f"Maximum temperature is: {max_temp}")

min_temp = data["temp"].min()
print(f"Minimum temperature is: {min_temp}")

#to get data in columns
#print(data.{column_name})
print(data.temp)
print(data.condition)

#get data in row
#first get hold of data table, then get the column you want to search through
#inside that column we can check for the row where the value is Monday
data[data["day"] == "Monday"]
#or

print(data[data.day == "Monday"])

#this will return the row of Monday that we want

print(data[data.temp == max_temp])

#we can also use rows to get the value
monday = data[data.day == "Monday"]
print(monday.condition)

#create a dataframe from scratch
data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

#how to create dataframe from this dictionary

df1 = pd.DataFrame(data_dict)
print(df1)

#we can convert the dataframe to csv
df1.to_csv("E:/CODING/GitHub Repositories/100-Days-of-Code/Day25/new_data.csv")