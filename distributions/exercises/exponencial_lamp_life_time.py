from scipy.stats import expon

# See more: https://docs.scipy.org/doc/scipy-1.15.2/reference/generated/scipy.stats.expon.html
print('''the mean life expectancy of a light bulb is 500 hours.
What is the probability that a light bulb will last less between 300 and 1000 hours?''')

mean = 500
lambda_ = 1 / mean

result = expon.cdf(1000, scale=1/lambda_) - expon.cdf(300, scale=1/lambda_)
print(result)


