# Mean Hipotesis tests for Normal distributed population - One-Sample Z-Test

# Example
# It is known that the duration of travels in a certain city is normally
# distributed with a mean of 300 and a standard deviation of 30 minutes.
# A sample of 10 travels is taken and the average duration is 314 minutes.
# Does this sample provide enough evidence that the average
# duration was right? Use a significance level (alpha) of 0.1

# null hypothesis (H0): mu = 300
# alternative hypothesis (H1): mu != 300 (two-tailed test)
mu = 300
sigma = 30
n = 10
x = 314
alpha = 0.1

# Critical value
from scipy.stats import t
t_critical = t.ppf(1 - alpha / 2, n - 1) # two-tailed test
print(f"Critical value: {t_critical}")


# p-value
# The p-value for two-tailed test is calculated as:
p_value = 2 * (1 - t.cdf(abs(t_critical), n - 1))

print(f"p-value: {p_value}")

if (p_value < alpha):
    print("Reject the null hypothesis")
else:
    print("Fail to reject the null hypothesis") 
    
