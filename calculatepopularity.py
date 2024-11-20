import math
from math import sqrt

import numpy as np
from scipy.stats import norm, lognorm


def calculate_weighted_ranking(rule_complexity_pages, viewership_millions,
                               accessibility_true, pace_score):
    # Constants for log-normal distribution (mean and std for CO2 emissions)
    co2_mean = 9979.50  # mean value for CO2 emissions
    co2_std = 6767.81  # standard deviation for CO2 emissions

    # Constants for normal distribution (mean and std for rule complexity)
    rule_mean = 99.08  # mean value for rule complexity in pages
    rule_std = 70.08  # standard deviation for rule complexity

    # Constants for log-normal distribution (mean and std for viewership)
    viewership_mean = 1.5229  # mean value for viewership in millions
    viewership_std = 0.8716  # standard deviation for viewership

    # Calculate Z-scores
    # z_co2 = pow(math.e,(((co2_emissions) - (co2_mean)) / ((co2_std) if co2_std > 0 else 1)))
    z_rule_complexity = (rule_complexity_pages - rule_mean) / (rule_std if rule_std > 0 else 1)
    z_viewership = sqrt((viewership_millions - viewership_mean) / (viewership_std if viewership_std > 0 else 1))

    # Assign weights to each factor
    weights = {
        # 'co2': 0.25,
        'rule_complexity': 0.25,
        'viewership': 0.25,
        'accessibility': 0.15,
        'pace': 0.10
    }

    # Calculate the weighted score
    weighted_score = (
            # weights['co2'] * z_co2 * -1+
            weights['rule_complexity'] * z_rule_complexity *-1+
            weights['viewership'] * z_viewership +
            weights['accessibility'] * (accessibility_true) +
            weights['pace'] * pace_score
    )

    return weighted_score


# usage:
ranking_score = calculate_weighted_ranking(
    # co2_emissions=1200,  # CO2 emissions in metric tons
    rule_complexity_pages=60,  # Complexity in pages
    viewership_millions=700,  # Viewership in millions
    accessibility_true=0.6,  # Accessibility flag
    pace_score=0.8  # Pace score from 0 to 1
)

print("Weighted Ranking Score:", ranking_score)