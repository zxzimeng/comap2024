import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Step 1: Define the sports and their number of rules
rules_count = [
    477, 95, 136, 41, 13, 76, 72, 60, 86, 75, 46, 274, 93, 221, 1264
]
# Step 2: Calculate Q1, Q3 and IQR to identify outliers
Q1 = np.percentile(rules_count, 25)
Q3 = np.percentile(rules_count, 75)
IQR = Q3 - Q1
# Define lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(upper_bound)

# Identify non-outlier values for mean calculation
non_outliers = [x for x in rules_count if lower_bound <= x <= upper_bound]

# Calculate mean and standard deviation of non-outliers
mean_rules = np.mean(non_outliers)
std_dev_rules = np.std(non_outliers)
# Print mean and standard deviation values
print(f"Mean number of rules (excluding outliers): {mean_rules:.2f}")
print(f"Standard deviation of rules (excluding outliers): {std_dev_rules:.2f}")

# Step 3: Create a histogram to visualize the distribution of rules
plt.figure(figsize=(10,6))
plt.hist(rules_count, bins=np.arange(0, 1400, 60), alpha=0.7, color='blue', edgecolor='black', density=True)

# Step 4: Generate x values for the normal distribution curve
x = np.linspace(min(rules_count) - 50, max(rules_count) + 50, 1000)
y = norm.pdf(x, mean_rules, std_dev_rules)

# Step 5: Overlay the normal distribution curve on the histogram
plt.plot(x, y, color='red', linewidth=2, label='Normal Distribution')

# Step 6: Customize plot
plt.title('Distribution of Rules in Various Sports with Normal Distribution Overlay')
plt.xlabel('Pages of Rules (Letter, 12pt)')
plt.ylabel('Density')
plt.xticks(np.arange(0,1300,100))
plt.grid(axis='y', alpha=0.75)
plt.legend()
plt.show()
