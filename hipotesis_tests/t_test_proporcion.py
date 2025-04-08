from scipy.stats import norm

# A factory says that at least 90% of its products do not have defects.
# A sample of 200 prospects is taken and 30 of them have defects.
# What can we say about the factory's claim? Use a significance level (alpha) of 0.2
# null hypothesis (H0): p >= 0.9
# alternative hypothesis (H1): p < 0.9

p = 0.9 # sample proportion of successes
n = 200 # sample size
x = 30 # number of defects
alpha = 0.2 # significance level

sample_proportion = 1 - x / n # proportion successes
print(f"Sample proportion: {sample_proportion}")


# check if the normal distribution can be used as approximation
if n * p >= 5 and n * (1 - p) >= 5:
    print("Normal distribution can be used as approximation")
else:
    print("Normal distribution cannot be used as approximation")



# Z test
z = (sample_proportion - p) / ((p * (1 - p)) / n) ** 0.5
print(f"Z test statistic: {z}")
# Critical value

z_critical = norm.ppf(1 - alpha)
print(f"Critical value: {z_critical}")

# p-value
p_value = norm.cdf(z)
print(f"p-value: {p_value}")