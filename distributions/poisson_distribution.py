from scipy.stats import poisson

print('Poisson Distribution')
print('---------------------')
print(
    'The Poisson distribution is a discrete probability distribution that expresses the probability of'
    'a given number of events occurring in a fixed interval of time or space, given that these events occur '
    'with a known constant mean rate and independently of the time since the last event.'
    'The formula for the Poisson distribution is:\n'
    'P(x) = (λ^x * e^(-λ)) / x!\n'
    'Where:\n'
    'P(x) = Probability of x events in a fixed interval\n'
    'λ = Average number of events in the interval\n'
    'e = Euler\'s number (approximately 2.71828)\n'
    'x = Number of events\n'
    'x! = Factorial of x\n'
    'The Poisson distribution is often used to model the number of events that occur within a given time period,'
    'such as the number of phone calls received at a call center in an hour, or the number of emails received in a day.'
)


# # probability mass function (exact)
# poisson.pmf(x, lambda_)

# # cumulative distribution function (<=)
# poisson.cdf(x, lambda_)

# # survival function (>)
# poisson.sf(x, lambda_)


print(
    'Example'
    'A bank knows that on average 6 customers buy a investiment every hour.'
    'What is the probability that exactly 2 customers will buy a investiment in the next hour?'
)

lambda_ = 6 # average number of events in the interval
x = 8 # number of events

print('Which is the probability of at least 8 customers buying a investiment in the next hour?')
print(poisson.sf(x-1, lambda_)) # survival function. -1 because sf does not include the value of x (< and not <=)

print('Which is the probability of less than 8 customers buying a investiment in the next hour?')
print(poisson.cdf(x-1, lambda_)) # cumulative distribution function. -1 because cdf includes the value, and we want to exclude it ("less than 8")

print('Which is the probability of having 18 customers buying a investiment in the next 4 hours?')
lambda_ = 6 * 4 # average number of events in the interval
x = 18 # number of events
print(poisson.pmf(x, lambda_)) # probability mass function

print('Which is the probability of having 24 customers buying a investiment in the next 4 hours?')
lambda_ = 6 * 4 # average number of events in the interval
x = 24 # number of events
print(poisson.pmf(x, lambda_)) # probability mass function


print('Which is the probability of having 30 customers buying a investiment in the next 4 hours?')
lambda_ = 6 * 4 # average number of events in the interval
x = 30 # number of events
print(poisson.pmf(x, lambda_)) # probability mass function

