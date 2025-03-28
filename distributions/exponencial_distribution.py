from scipy.stats import expon

# See more: https://docs.scipy.org/doc/scipy-1.15.2/reference/generated/scipy.stats.expon.html

print('''
'Exponential Distribution'    
'---------------------'

The exponential distribution is a continuous probability distribution that describes the time between events in a Poisson process.

f(x) = λ * e^(-λx)
Where:
f(x) = Probability density function
λ = Rate parameter (average number of events per unit time). It is the inverse of the mean (1/μ)
e = Euler's number (approximately 2.71828)
x = Time between events, > 0

The exponential distribution is often used to model the time until an event occurs, such as the time until a radioactive particle decays, 
or the time until a customer arrives at a service point.

P(a < X < b) = ∫[a, b] f(x) dx = e^(-λa) - e^(-λb)

''')
# # probability density function (exact): expon.pdf(x, lambda_) = 0: Always zero because this is a continuous distribution
# cumulative distribution function (<): expon.cdf(x, lambda_)
# survival function (>): expon.sf(x, lambda_)


print('''
'Example'
'---------------------'
The life expectancy (hours) of a certain type of light bulb is modeled by an exponential distribution with a rate parameter of 1/8000 .
Which is the average life expectancy of the light bulb?
''')


# Parameters
lambda_ = 1 / 8000  # Rate parameter
average = 1/ lambda_  # Time in hours

print('The average life expectancy of the light bulb is: ${:.2f} hours'.format(average))

print('Find the probability that a light bulb lasts for at least 4.000 hours.')

# P (4000 <= X < ∞) = 1 - P (X < 4000) = 1 - P (a=0, b=4000) 
# = 1 - { eˆ(-λ*0) - eˆ(-λ*4000) }
# = 1 - { eˆ(0) - eˆ(-λ*4000) }
# = 1 - { 1 - eˆ(-λ*4000) }
# = eˆ(-λ*4000)
# = eˆ(-4000/8000)
# = eˆ(-0.5) = 0.6065306597

result = expon.sf(4000, scale=1/lambda_)
print(result)


print('Which is the probability of a bulb lasting less than 50 hours?')
result = expon.cdf(50, scale=1/lambda_)
print(result)

print('Which is the probability of a bulb lasting for 10.000 hours given that it has already lasted for 6.000 hours?')
# P (X >= 10000 | X >= 6000)
# Memoryless property
# The memoryless property states that the future lifetime of a system is independent of its past lifetime.
# As the bulb has already lasted for 6000 hours, we can ignore this time and consider the remaining lifetime.
# P (X >= 10000 | X >= 6000) = P (X >= 10000 - 6000) = P (X >= 4000)
result = expon.sf(4000, scale=1/lambda_)
print(result)

print('''
* For the bulb example the exponential distributionas might not be the best fit, as the Memoryless Property does not apply. 
The life expectancy of a light bulb is not independent of its past life.
This distribution is more suitable for modeling things like the time until a radioactive particle decays, or the time waiting in a queue.   
''')



print('The waiting time in a queue is modeled by an exponential distribution with a rate parameter of 1/5 minutes.')

print('Which is the probablity of waiting less the meaning time?')
lambda_ = 1 / 5  # Rate parameter
mean = 1/lambda_ # Time in minutes
# P (X < mean) = P (X < 5) 
result = expon.cdf(mean, scale=1/lambda_)
print(result)