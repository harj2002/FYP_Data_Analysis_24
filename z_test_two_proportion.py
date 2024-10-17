from math import sqrt
from scipy.stats import norm


def two_proportion_z_test(data):
    """
    Perform a two-proportion z-test and return the p-value.

    Parameters:
    x1 (int): Number of successes in the first sample (e.g., number of participants when the confederate is absent).
    n1 (int): Total number of observations in the first sample.
    x2 (int): Number of successes in the second sample (e.g., number of participants when the confederate is present).
    n2 (int): Total number of observations in the second sample.

    Returns:
    float: p-value for the z-test.
    """
    x1, n1, x2, n2 = data

    # Sample proportions
    p1 = x1 / n1
    p2 = x2 / n2

    # Pooled proportion
    p = (x1 + x2) / (n1 + n2)

    # Standard error
    standard_error = sqrt(p * (1 - p) * (1 / n1 + 1 / n2))

    # Z-test statistic
    z = (p1 - p2) / standard_error
    print(f'z-Value: {z}')


    # Calculate the p-value for a two-tailed test
    p_value = 2 * (1 - norm.cdf(abs(z)))

    return p_value

# Participation
confed_participation = [427, 974, 410, 1100]
# Behaviours
NS_vs_EF = [90, 90+48+10, 143, 143+27+5]
NS_vs_ATE = [90, 90+48+10, 148, 148+25+8]
ATE_vs_EF = [148, 148+25+8,143, 143+27+5]
EF_vs_ATE = [143, 143+27+5, 148, 148+25+8]
# Confederate
Abs_vs_Pres = [242,242+80+20,232,232+68+12]


p_value = two_proportion_z_test(Abs_vs_Pres)
print(f"The p-value for confederate compliance is: {p_value:.10f}")
