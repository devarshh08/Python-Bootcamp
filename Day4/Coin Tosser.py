while True:
  print("Welcome to the coin tosser:")
  ch = input('''Enter anything to start\n''')
  print("Tossing the coin...")
  print("  ")
  import random
  toss = random.randint(0,1)
  if toss == 0:
    print("Tails \n \n")
  elif toss == 1:
    print("Heads \n \n")