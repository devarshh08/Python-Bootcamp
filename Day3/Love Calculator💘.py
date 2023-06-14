while True:
  print("Welcome to Love Calculator💘")
  name_1 = input("What is your name? \n")
  name_2 = input("What is their name? \n")
  
  name1 = name_1.lower()
  name2 = name_2.lower()
  
  dig1 = 0
  dig2 = 0
  for i in name1:
    if i == 't' or i == 'r' or i == 'u' or i == 'e':
      dig1 += 1
  
    if i == 'l' or i == 'o' or i == 'v' or i == 'e':
      dig2 +=1
  
  for i in name2:
    if i == 't' or i == 'r' or i == 'u' or i == 'e':
      dig1 += 1
  
    if i == 'l' or i == 'o' or i == 'v' or i == 'e':
      dig2 +=1
  
  
  print("Your love percentage is "+str(dig1)+str(dig2)+"%")