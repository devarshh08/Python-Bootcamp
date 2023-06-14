def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number%i == 0:
      is_prime = False
    
  if is_prime == True:
    print("Prime number")
  else:
    print("Not prime")
      

while True:
  number = int(input("Enter number to check: "))
  prime_checker(number)
