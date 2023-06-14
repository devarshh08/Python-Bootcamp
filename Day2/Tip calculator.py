print("Welcome to the tip calculator:")
bill = float(input("What was the total bill? "))
count = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? "))
total = (bill + (bill*(tip/100)))/count
amt = round(total, 2)
print("Each person should pay: ", amt)