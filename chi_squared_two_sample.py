# Import necessary libraries
import numpy as np
from scipy.stats import chi2

# Two-Sample Comparisons with Categorical Data

def chi_squared_two_sample(observed):
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
    print(f"Chi-square statistic: {chi_square_statistic:.3f}")
    print(f"Degrees of freedom: {df}")
    print(f"P-value: {p_value:.6f}")

    # Conclusion based on significance levels
    alpha_5 = 0.05   # Significance level of 5%

    if p_value < alpha_5:
        print("Reject the null hypothesis at the 5% significance level.")
    else:
        print("Fail to reject the null hypothesis.")


def main():
    # Observed data from the study
    # Row 1: HIT, Row 2: MISS
    # Column 1: Behaviour 1, Column 2: Behaviour 2
    # Python format: [[(row 1 col 1) , (row 1 col 2)],[(row 2 col 1) , (row 2 col 2)]]
    observed = np.array([
                            [[93, 31], [57, 55]],     # H1 
                                                            #Base Case Hits:93, Miss: 57
                                                            #No Robot  Hits:31, Miss: 55
                            [[93, 90], [57, 58]],     # H2      
                                                            #Base Case Hits:93, Miss: 57
                                                            #Neutral   Hits:90, Miss: 58
                            [[143, 90], [32, 58]],    # H3      
                                                            #Evoking   Hits:143,Miss: 32
                                                            #Neutral   Hits:90, Miss: 58
                            [[148, 90], [33, 58]],    # H4      
                                                            #ATE       Hits:148,Miss: 33
                                                            #Neutral   Hits:90, Miss: 58
                            [[143, 148], [32, 33]],   # H5      
                                                            #Evoking   Hits:143,Miss: 32    
                                                            #ATE       Hits:148,Miss: 33
                            [[232, 242], [80, 100]],  # H6
                                                            #With Conf Hits:232,Miss: 80    
                                                            #Wout Conf Hits:242,Miss: 100
                            [[427, 410], [547, 690]], # H7
                                                            #With Conf Hits:427,Miss: 547    
                                                            #Wout Conf Hits:410,Miss: 690
                        ])
    obs_sum = np.sum(np.sum(observed,1),1)
    for hypot,obs in enumerate(observed):
        print(f"\nH{hypot+1}")
        print(f"Sample size:{obs_sum[hypot]}")
        chi_squared_two_sample(obs)


if __name__ == "__main__":
    main()
