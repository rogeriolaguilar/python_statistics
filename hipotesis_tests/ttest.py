import pingouin
weight = [12,8,15,13,10,12,14,11,12,13,15,19,15,12,13,16,15]

# A researcher wants to test if the average weight loss of a group of people is greater than 12 kg. He want it to be 95% sure of the result (5% of significance level).

# null hypothesis (H0): <= 12
# alternative hypothesis (H1): > 12
H0 = 12
alternative = 'greater' # one-tailed test
confidence = 0.95

result = pingouin.ttest(x=weight, y=H0,alternative="greater", confidence=confidence)

print(result)


# Example output:
'''
               T  dof alternative     p-val         CI95%  cohen-d   BF10     power
T-test  2.006838   16     greater  0.030985  [12.16, inf]  0.48673  2.494  0.608764
'''
# Meaning:
# T: test statistic
# dof: degrees of freedom (number of observations - 1)
# alternative: type of test (one-tailed or two-tailed)
# p-val: p-value (probability of observing the data given the null hypothesis is true)
# CI95%: 95% confidence interval

# As p-val is less than 0.05, we reject the null hypothesis and accept the alternative hypothesis.
# The average weight loss of the group is greater than 12 kg.