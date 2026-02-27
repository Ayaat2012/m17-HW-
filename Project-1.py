# Importing necessary library
import random

# Finding out the probability of getting a 6 on the first roll of a 6-sided dice
print("Probability of getting a 6 is", 1/6)

# Rolling the dice now
roll = random.randint(1, 6)
print("Dice rolled...")
print(f"It landed on {roll}")

if roll == 6:
    print("The game can be started!")
else:
    print("Roll again. Best of luck!")