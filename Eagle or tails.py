import random
combination = input("Eagle or Tails?")
win = random.choice(["Eagle", "Tails"])
if win == combination:
   print("Win")
else:
   print("Lose")

