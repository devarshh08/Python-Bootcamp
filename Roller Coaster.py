while True:
  height = int(input("Height? "))
  age = int(input("Age? "))
  
  if height < 120:
    print("You cannot ride")
  elif height>120:
    print("You can ride")
    photo = input("Do you want a photo? Answer in Y or N ")
    if age < 12:
      if photo == "Y" or photo == "y":
        print("8 dollar")
      elif photo == "N" or photo == "n":
        print("5 dollar")
    elif age > 12 and age < 18:
      if photo == "Y" or photo == "y":
        print("10 dollar")
      elif photo == "N" or photo == "n":
        print("7 dollar")
    elif age > 18:
      if photo == "Y" or photo == "y":
        print("15 dollar")
      elif photo == "N" or photo == "n":
        print("12 dollar")
    else:
      print("Enter a valid age")
  else:
    print("Enter a valid height")