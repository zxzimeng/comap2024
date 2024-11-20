import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import lognorm, skew, kurtosis

# Step 1: Input the expanded viewership data (in millions)
viewership_data = np.array([
    123.4,  # NFL Super Bowl
    17.9,   # NFL Regular Season Average
    12.2,   # NBA Finals
    9.11,   # MLB World Series
    2.76,   # NHL Stanley Cup Finals
    25.78,  # FIFA World Cup Final
    2.76,   # UEFA Champions League Final
    5.3,    # Indy 500
    2.38,   # U.S. Open (Golf)
    1.53,   # WNBA Game
    1.9,    # NCAA Women's College World Series
    1.8,    # Formula 1 Canadian Grand Prix
    0.546,  # Premier League Match Average
    2600,   # Cricket World Cup
    3500,   # Tour de France
    3.5,    # Australian Open (Tennis)
    2.3,    # Wimbledon (Tennis)
    15.5,   # Summer Olympics (average)
    2.0     # Winter Olympics (average)
])

# Step 2: Remove outliers using IQR method
Q1 = np.percentile(viewership_data, 25)
Q3 = np.percentile(viewership_data, 75)
IQR = Q3 - Q1

# Define bounds for outliers
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter the viewership data to remove outliers
filtered_viewership_data = viewership_data[(viewership_data >= lower_bound) & (viewership_data <= upper_bound)]

# Print filtered data for verification
print("Filtered Viewership Data (without outliers):")
print(filtered_viewership_data)

# Step 3: Calculate basic statistics on filtered data
mean_viewership = np.mean(filtered_viewership_data)
std_dev_viewership = np.std(filtered_viewership_data)
median_viewership = np.median(filtered_viewership_data)
data_skewness = skew(filtered_viewership_data)
data_kurtosis = kurtosis(filtered_viewership_data)
viewership_range = np.max(filtered_viewership_data) - np.min(filtered_viewership_data)

# Print calculated metrics for filtered data
print(f"\nMean of viewership: {mean_viewership:.2f} million")
print(f"Standard Deviation of viewership: {std_dev_viewership:.2f} million")
print(f"Median of viewership: {median_viewership:.2f} million")
print(f"Skewness of viewership: {data_skewness:.4f}")
print(f"Kurtosis of viewership: {data_kurtosis:.4f}")
print(f"Range of viewership: {viewership_range:.2f} million")

# Step 4: Calculate parameters for the log-normal distribution using filtered data
mu = np.log(mean_viewership**2 / np.sqrt(std_dev_viewership**2 + mean_viewership**2))
sigma = np.sqrt(np.log(1 + (std_dev_viewership**2 / mean_viewership**2)))

print(f"\nParameters for Log-Normal Distribution:")
print(f"mu (location parameter): {mu:.4f}")
print(f"sigma (scale parameter): {sigma:.4f}")

# Step 5: Generate x values from a small value to a large value for plotting
x = np.linspace(0, max(filtered_viewership_data) * 2, 1000)

# Step 6: Calculate the probability density function (PDF) for the log-normal distribution
pdf = lognorm.pdf(x, s=sigma, scale=np.exp(mu))

# Step 7: Plotting the log-normal distribution and histogram based on filtered data
plt.figure(figsize=(10, 6))

# Histogram of the filtered viewership data
plt.hist(filtered_viewership_data, bins=10, density=True, alpha=0.5, color='blue', label='Histogram of Viewership Data')

# Log-normal distribution plot
plt.plot(x, pdf, color='blue', label='Log-Normal Distribution', linewidth=2)
plt.fill_between(x, pdf, color='skyblue', alpha=0.5)

# Adding titles and labels
plt.title('Log-Normal Distribution of Sports Viewership (Outliers Removed)')
plt.xlabel('Viewership (in millions)')
plt.ylabel('Probability Density')
plt.axvline(mean_viewership, color='red', linestyle='--', label='Mean Viewership')
plt.axvline(median_viewership, color='orange', linestyle='--', label='Median Viewership')
plt.axvline(mean_viewership + std_dev_viewership, color='green', linestyle='--', label='1 Std Dev')
plt.axvline(mean_viewership - std_dev_viewership, color='green', linestyle='--')

# Adding legend and grid
plt.legend()
plt.grid()
plt.xlim(0, max(filtered_viewership_data) * 2)
plt.ylim(0, max(pdf) * 1.1)
plt.show()