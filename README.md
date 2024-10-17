# Investigating the Dynamics of Robot Induced Social Influence
# ENG4701/FIT4701: Final Year Project - GITHUB

This repository contains Python scripts for analyzing experimental data from the Pepper robot experiments. The scripts focus on performing statistical tests for two-sample comparisons using categorical data, specifically chi-square tests and two-proportion z-tests. These analyses help assess hypotheses related to behaviors and interactions observed in the experiment.

## Files

### `chi_squared_two_sample.py`
This script performs chi-square tests for independence on categorical data. It tests whether observed behaviors across different conditions are statistically independent or significantly different.

- **Functions:**
  - `chi_squared_two_sample(data)`: Takes a 2x2 matrix of observed values and performs a chi-square test to compare two groups, outputting the chi-square statistic, degrees of freedom, and p-value.
  - `main()`: Contains predefined data representing the experiment results and runs chi-square tests on each hypothesis (H1 to H7).

### `z_test_two_proportion.py`
This script conducts two-proportion z-tests, a statistical method used to compare the proportions between two independent groups.

- **Functions:**
  - `two_proportion_z_test(data)`: Takes the number of successes and total observations for two samples and performs a z-test to compare the proportions, outputting the z-value and p-value.

- **Predefined Comparisons:**
  - Confederate presence/absence participation (Abs_vs_Pres).
  - Behavioral comparisons between different conditions (e.g., NS vs. EF, ATE vs. EF).

## Usage
Run the scripts from the command line or within a Python environment to perform the statistical tests:

```
python chi_squared_two_sample.py
python z_test_two_proportion.py
```

Each script outputs relevant statistical metrics, including chi-square or z-test statistics and corresponding p-values, along with conclusions regarding the null hypothesis for each comparison.

## Dependencies
These scripts require the following Python libraries:
numpy
scipy
Install the necessary dependencies with:
```
pip install numpy scipy
```
