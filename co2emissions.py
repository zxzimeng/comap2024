import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm

# Step 1: Input the carbon footprint data for specific sports events (in kg CO2e)
carbon_footprint_data = np.array([
    13700,    # NBA Game (per game)
    12200,    # NHL Game (per game)
    5600,     # MLB Game (per game)
    4300,     # Marathon Running (including travel)
    2195,     # Golf Tournament (per event)
    2841      # Skydiving (per jump)
])

# Step 2: Calculate Q1, Q3 and IQR to identify outliers
Q1 = np.percentile(carbon_footprint_data, 25)
Q3 = np.percentile(carbon_footprint_data, 75)
IQR = Q3 - Q1

# Define lower and upper bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print(f"Upper Bound for Outliers: {upper_bound:.2f}")

# Identify non-outlier values for mean calculation
non_outliers = [x for x in carbon_footprint_data if lower_bound <= x <= upper_bound]

# Calculate parameters for the log-normal distribution using non-outlier data
mean_non_outliers = np.mean(non_outliers)
std_dev_non_outliers = np.std(non_outliers)

# Calculate parameters for the log-normal distribution
mu = np.log(mean_non_outliers**2 / np.sqrt(std_dev_non_outliers**2 + mean_non_outliers**2))
sigma = np.sqrt(np.log(1 + (std_dev_non_outliers**2 / mean_non_outliers**2)))

# Print mean and standard deviation values
print(f"Mean Carbon Footprint (excluding outliers): {mean_non_outliers:.2f} kg CO2e")
print(f"Standard Deviation of Carbon Footprint (excluding outliers): {std_dev_non_outliers:.2f} kg CO2e")


# Step 3: Create a histogram to visualize the distribution of carbon footprints
plt.figure(figsize=(10, 6))
plt.hist(carbon_footprint_data, bins=np.arange(0, 22000, 1200), alpha=0.6, color='blue', edgecolor='black', density=True)

# Step 4: Generate x values for the log-normal distribution curve
x = np.linspace(min(carbon_footprint_data) - 500, max(carbon_footprint_data) + 500, 1000)
y = lognorm.pdf(x, s=sigma, scale=np.exp(mu))

# Step 5: Overlay the log-normal distribution curve on the histogram
plt.plot(x, y, color='red', linewidth=2, label='Log-Normal Distribution')

# Step 6: Customize plot
plt.title('Distribution of Carbon Footprints in Various Sports with Log-Normal Distribution Overlay')
plt.xlabel('Carbon Footprint (kg CO2e)')
plt.ylabel('Density')
plt.xticks(np.arange(0, 22000, 2000))
plt.grid(axis='y', alpha=0.75)
plt.ylim(0,0.000170)
plt.legend()
plt.show()