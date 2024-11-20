import numpy as np
from scipy.stats import lognorm
import matplotlib.pyplot as plt


def create_distribution(prices, region_name):
    mu = np.mean(np.log(prices))
    sigma = np.std(np.log(prices))
    dist = lognorm(s=sigma, scale=np.exp(mu))

    x = np.linspace(0, max(prices) * 1.2, 1000)
    plt.figure(figsize=(10, 6))
    plt.plot(x, dist.pdf(x))
    plt.title(f'Log-Normal Distribution of Olympic Streaming Costs - {region_name}')
    plt.xlabel('Monthly Cost ($)')
    plt.ylabel('Probability Density')
    plt.grid(True)
    plt.show()

    print(f"{region_name} Statistics:")
    print(f"Mean cost: ${dist.mean():.2f}")
    print(f"Median cost: ${dist.median():.2f}")
    # print(f"Mode cost: ${dist.mode():.2f}\n")

    return dist


# North American/European prices
na_eu_prices = np.array([7.99, 76.99, 72.99, 79.99, 45, 109.99])
na_eu_dist = create_distribution(na_eu_prices, "North American/European")

# Asian/East Asian prices
asian_prices = np.array([5.99, 39.99, 29.99, 49.99, 19.99])
asian_dist = create_distribution(asian_prices, "Asian/East Asian")

# Combined distribution
plt.figure(figsize=(10, 6))
x = np.linspace(0, 150, 1000)
plt.plot(x, na_eu_dist.pdf(x), label='North American/European')
# plt.plot(x, asian_dist.pdf(x), label='Asian/East Asian')
plt.title('Combined Log-Normal Distributions of Olympic Streaming Costs')
plt.xlabel('Monthly Cost ($)')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()

# Percentage already subscribed
already_subscribed = 0.71
print(f"Estimated percentage already subscribed: {already_subscribed:.2%}")