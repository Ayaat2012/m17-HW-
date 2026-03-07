# Find and calculate the probability of observing between 2 and 4 heads from 10 coin flips using PMF(Probability Mass Function)
import scipy.stats as stats

trials = 10
prob_head = 0.5

k_values = [2, 3, 4]

probabilities = stats.binom.pmf(k_values, trials, prob_head)

total_prob = sum(probabilities)

print(f"Probabilities for {k_values} heads in {trials} flips:")
for k, prob in zip(k_values, probabilities):
    print(f"P(X = {k}) = {prob:.4f}")

print(f"\nThe probability of observing between {min(k_values)} and {max(k_values)} heads in {trials} flips is: {total_prob:.4f}")