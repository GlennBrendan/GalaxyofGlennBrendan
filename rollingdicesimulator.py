# Simulate Rolling Dice Exercise - variation of coinflip

import random
dice_result = random.randrange(1,7)

# test import of random correctly by running print dice result 
print dice_result

# test each variable comes up after a die throw - use 100 iterations to test
import datetime 
now = datetime.datetime.now() 
random.seed(now)
for k in range(0,100):
    print(random.randrange(1,7))

# replace coinsides with dice sides, set all to 0

Side_1 = 0
Side_2 = 0
Side_3 = 0
Side_4 = 0
Side_5 = 0
Side_6 = 0

# set up range of 1000 iterations for diceroll with possible outcomes between 1 and 6

for x in range(0, 1000):
  DiceRoll = random.randrange(1,7)
  if DiceRoll == 1:
    Side_1 += 1
  elif DiceRoll == 2:
    Side_2 += 1
  elif DiceRoll == 3:
    Side_3 += 1
  elif DiceRoll == 4:
    Side_4 += 1
  elif DiceRoll == 5:
    Side_5 += 1
  elif DiceRoll == 6:
    Side_6 += 1

# set up mumber of each dice face outcome to print as a vector

print ("1: %d") % (Side_1)
print ("2: %d") % (Side_2)
print ("3: %d") % (Side_3)
print ("4: %d") % (Side_4)
print ("5: %d") % (Side_5)
print ("6: %d") % (Side_6)
