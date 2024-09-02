# Import necessary libraries
import numpy as np
from scipy.stats import chi2

# Section 4.5: Two-Sample Comparisons with Categorical Data

def twoSampleTest(observed):
    # Total number of observations
    total_observed = np.sum(observed)

    # Calculate row and column sums
    row_sums = np.sum(observed, axis=1)
    col_sums = np.sum(observed, axis=0)

    # Calculate expected frequencies under the null hypothesis
    expected = np.outer(row_sums, col_sums) / total_observed

    # Calculate the chi-square statistic
    chi_square_statistic = np.sum((observed - expected) ** 2 / expected)

    # Degrees of freedom (df = (number of rows - 1) * (number of columns - 1))
    df = (observed.shape[0] - 1) * (observed.shape[1] - 1)

    # Calculate the p-value
    p_value = 1 - chi2.cdf(chi_square_statistic, df)

    # Output the results
    # print(f"Chi-square statistic: {chi_square_statistic:.3f}")
    print(f"Degrees of freedom: {df}")
    print(f"P-value: {p_value:.6f}")

    # Conclusion based on significance levels
    # alpha_10 = 0.10  # Significance level of 10%
    alpha_5 = 0.05   # Significance level of 5%

    if p_value < alpha_5:
        print("Reject the null hypothesis at the 5% significance level.")
    # elif p_value < alpha_10:
    #     print("Reject the null hypothesis at the 10% significance level, but not at the 5% level.")
    else:
        print("Fail to reject the null hypothesis.")


def main():
    # Observed data from the study
    # Row 1: HIT, Row 2: MISS
    # Column 1: Behaviour1, Column 2: Behaviour12
    observed = np.array([[[143, 90], [32, 58]],    # Table 1
                              [[148, 90], [33, 58]],    # Table 2
                              [[148, 143], [33, 32]],   # Table 3
                              [[232, 242], [80, 100]]])
    for hypot,obs in enumerate(observed):
        print(f"\nH{hypot+1}")
        twoSampleTest(obs)

if __name__ == "__main__":
    main()
