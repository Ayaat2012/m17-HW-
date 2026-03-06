# -------- Event Descriptions --------

dependence = "We pick two cards from a deck WITHOUT replacement. Event A: first card is an Ace. Event B: second card is an Ace."

mutually_exclusive = "We roll a dice once. Event A: rolling a 2. Event B: rolling a 5."

not_mutually_exclusive = "We roll a dice once. Event A: rolling an odd number. Event B: rolling a number greater than four."

independent = "We flip a coin and roll a die. Event A: coin is Heads. Event B: die shows 6."


# -------- Event List with Correct Answers --------
# 1 = dependent
# 2 = independent
# 3 = mutually exclusive
# 4 = not mutually exclusive

events = [
    (dependence, 1),
    (independent, 2),
    (mutually_exclusive, 3),
    (not_mutually_exclusive, 4),
]


# -------- Quiz Function --------

def guess_the_type(event, correct_answer):

    print("\nGuess the event type:")
    print("1) Dependent")
    print("2) Independent")
    print("3) Mutually Exclusive")
    print("4) Not Mutually Exclusive\n")

    print(event)

    answer = int(input("Enter your answer: "))

    if answer == correct_answer:
        print("\n✅ Correct!\n")
        return True
    else:
        print("\n❌ Wrong answer.\n")
        return False


# -------- Run Quiz --------

score = 0

for event, ans in events:
    if guess_the_type(event, ans):
        score += 1


# -------- Result --------

if score == len(events):
    print("\n🎉 You guessed all events correctly! Here are cookies: 🍪🍪🍪")
else:
    print(f"\nYou got {score}/{len(events)} correct. Keep practicing!")