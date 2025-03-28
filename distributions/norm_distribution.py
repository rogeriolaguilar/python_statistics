from scipy.stats import norm

print('''
'Normal Distribution'
'---------------------'
The normal distribution, also known as the Gaussian distribution, is a continuous probability distribution that is symmetric about the mean.
It describes data that clusters around a mean or average. The normal distribution is characterized by its bell-shaped curve.
The normal distribution is defined by two parameters: 
- the mean (μ) 
- standard deviation (sd - σ).

The probability density function (PDF) of the normal distribution is given by:

f(x) = (1 / (sd * √(2π))) * e^(-((x - μ)² / (2sd²)))

Where:
- f(x) = Probability density function
- x = Value for which you want to calculate the probability
- μ = Mean of the distribution
- sd = Standard deviation of the distribution
- e = Euler's number (approximately 2.71828)
- π = Pi (approximately 3.14159)

''')


print('''
      The Port of South Louisiana distributes a mean of 4.5 million tons of cargo per week with a standard deviation of 0.82 million tons.
      ''')

mean = 4.5  # Mean in million tons
sd = 0.82  # Standard deviation

print('Which is the probability of the port distributing less than 5 million tons of cargo in a week?')

result = norm.cdf(5, mean, sd) # cumulative distribution function (CDF)
print('Probability:', result)


print('Which is the probability of the port distributing more than 3 million tons of cargo in a week?')
result = norm.sf(3, mean, sd)
print('Probability:', result)

print('Which is the probability of the port distributing between 3 and 4 million tons of cargo in a week?')
result = norm.cdf(4, mean, sd) - norm.cdf(3, mean, sd)
print('Probability:', result)

print('What is the value of cargo distributed in the 95th percentile?')
result = norm.ppf(0.95, mean, sd)  # Percent point function (inverse of CDF)
print('Value:', result)

