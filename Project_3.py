#There are 1 red ball, 6 blue balls and 3 white balls in as basket.
#If the two balls you pick out are white, then you win a prize.
# Find the probability that the second ball is also white given that the first ball is white
#(Assume that the first ball is replaced)


red_balls = 1
blue_balls = 6
white_balls = 3

total = red_balls + blue_balls + white_balls

#Since the first ball is replaced, the events are independent.
#The probability of picking a white ball on the second draw is the same
#as the probability of picking a white ball on the first draw.
prob_w_2_given_w_1 = white_balls / total

print(f"Probability that the second ball is white, given the first ball was white and replaced, is:{prob_w_2_given_w_1:.2f}")