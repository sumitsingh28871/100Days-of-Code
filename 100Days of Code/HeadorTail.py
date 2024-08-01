import random

#Greetings
print("Welcome to the Head or Tail program.")

random_side = random.randint(0,1)
if random_side == 0:
    print("Head")
else:
    print("Tails")