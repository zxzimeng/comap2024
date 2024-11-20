import numpy as np
from scipy.stats import lognorm
import matplotlib.pyplot as plt


def create_distribution(prices, name, color):
    mu, sigma = np.mean(np.log(prices)), np.std(np.log(prices))
    dist = lognorm(s=sigma, scale=np.exp(mu))

    x = np.linspace(0, np.max(prices) * 1.2, 1000)
    y = dist.pdf(x)

    plt.plot(x, y, label=name, color=color)
    return dist


# Generate data for each component
np.random.seed(42)  # for reproducibility

# Define colors for each distribution
colors = {
    "Hotel": 'blue',
    "Airfare": 'orange',
    "Visa": 'green',
    "Local Transportation": 'red',
    "Food and Entertainment": 'purple',
    "Olympic Event Tickets": 'brown',
    "Travel Insurance": 'pink'
}

# Generate random prices for each component
hotel_prices = np.random.uniform(1000, 4000, 1000)  # $100-$400 per night
airfare_prices = np.random.uniform(800, 3000, 1000)
visa_prices = np.random.uniform(0, 150, 1000)  # Some countries don't need visa
transport_prices = np.random.uniform(200, 500, 1000)  # For the entire trip
food_entertainment_prices = np.random.uniform(500, 1500, 1000)  # For the entire trip
ticket_prices = np.random.uniform(300, 2000, 1000)  # Multiple events
insurance_prices = np.random.uniform(100, 300, 1000)

# Create distributions for each component and plot them
plt.figure(figsize=(12, 8))

create_distribution(hotel_prices, "Hotel", colors["Hotel"])
create_distribution(airfare_prices, "Airfare", colors["Airfare"])
create_distribution(visa_prices, "Visa", colors["Visa"])
create_distribution(transport_prices, "Local Transportation", colors["Local Transportation"])
create_distribution(food_entertainment_prices, "Food and Entertainment", colors["Food and Entertainment"])
create_distribution(ticket_prices, "Olympic Event Tickets", colors["Olympic Event Tickets"])
create_distribution(insurance_prices, "Travel Insurance", colors["Travel Insurance"])

# Customize the plot
plt.title('Cost Distributions for Attending the 2032 Brisbane Olympics')
plt.xlabel('Cost ($)')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
plt.figure(figsize=(15, 12))

# Calculate total trip cost distribution
total_prices = (hotel_prices + airfare_prices + visa_prices + transport_prices +
                food_entertainment_prices + ticket_prices + insurance_prices)

# Create total cost distribution and plot it on the same graph
total_dist = create_distribution(total_prices, "Total Trip Cost", 'black')

# Show updated plot with total cost included
plt.title('Cost Distributions for Attending the 2032 Brisbane Olympics (Including Total Cost)')
plt.xlabel('Cost ($)')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()