'''
RULES OF THE GAME ARE:
Say Fizz if the number is divisible by 3.
Say Buzz if the number is divisible by 5.
Say FizzBuzz if the number is divisible by both 3 and 5.
Return the number itself, if the number is not divisible by 3 and 5.
'''


while True:
  print("Welcome to Fizz Buzz")
  ch = input("Enter anything to start: ")
  for i in range(1,101):
    if i%3 == 0:
      if i%5 == 0:
        print("FizzBuzz")
      else:
        print("Fizz")
    elif i%5 == 0:
      if i%3 == 0:
        print("FizzBuzz")
      else:
        print("Buzz")
    elif i%3 != 0 and i%5 != 0:
      print(i)