from scipy.stats import binom

print('Binomial Distribution')
print('---------------------')
print(
    'The binomial distribution model is given by the formula:\n'
    'P(x) = C(n, x) * p^x * (1 - p)^(n - x)\n'
    'Where:\n'
    'P(x) = Probability of x successes in n trials\n'
    'C(n, x) = Number of combinations of n items taken x at a time. The order of the items does not matter.\n'
    'p = Probability of success in a single trial\n'
    'n = Number of trials\n'
    'x = Number of successes\n'
)

n = 12
p = 0.05

def print_response(r):
    rounded = round(r*100, 2)
    print(f'{rounded}%')

print(f'Each box has {n} eggs. Eggs has a {p * 100}% chance of being rotten.')
print()
print('What is the probability of finding 2 rotten eggs in a box?')
r = binom.pmf(2, n, p)
print_response(r)

print()
print('What is the probability of finding 2 or less rotten eggs in a box?')
r = binom.cdf(2, n, p)
print_response(r)

print()
print('What is the probability of finding more than 2 rotten eggs in a box?')
r = binom.sf(2, n, p)
print_response(r)