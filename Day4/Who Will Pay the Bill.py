import random
while True:
  names = input('''Enter names of all people seperated by a space( )\n''')
  names_list = names.split(" ")
  num_of_persons = len(names_list)
  who_will_pay = random.randint(0,num_of_persons-1)
  print(f"{names_list[who_will_pay]} will pay the bill \n")