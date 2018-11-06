import random
print("I'm thinking of a number between 1 and 10.")
try:
  user_entry = int(input('Please guess what it is:'))
except ValueError:
  print("D'oh! That is NOT a number, Bart!")
  continue
  target = random.randint(1,10)
  while target != user_entry:
    if target > user_entry:
      print("That is too low!")
      user_entry = int(input('Please try again:'))
    if target < user_entry:
      print("That is too high!")
      user_entry = int(input('Please try again:'))
  print("That's it! You win!")
