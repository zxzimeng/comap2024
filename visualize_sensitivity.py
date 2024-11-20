# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def visualize_sensitivity():
#     # Define variables and their base values
#     variables = {
#         'Rule Complexity': 70,
#         'Viewership': 1.5,
#         'Accessibility Score': 0.75,
#         'Gender Ratio': 0.5,
#         'Building Costs': 300,
#         'Injury Rate': 0.2
#     }
#
#     # Define the range of variation for each variable (as a percentage)
#     variation_range = np.linspace(-20, 20, 41)  # -20% to +20% in 1% steps
#
#     # Calculate the effect on final score for each variable
#     effects = {}
#     for var, base_value in variables.items():
#         effects[var] = []
#         for variation in variation_range:
#             new_value = base_value * (1 + variation / 100)
#             # Simulate the effect on final score (this is a placeholder calculation)
#             effect = (new_value - base_value) / base_value * 100
#             effects[var].append(effect)
#
#     # Create the plot
#     fig, ax = plt.subplots(figsize=(12, 8))
#
#     # Plot each variable
#     colors = plt.cm.rainbow(np.linspace(0, 1, len(variables)))
#     for (var, effect), color in zip(effects.items(), colors):
#         ax.plot(variation_range, effect, label=var, color=color)
#
#     # Set up the plot
#     ax.set_xlabel('Variation from Base Value (%)')
#     ax.set_ylabel('Effect on Final Score (%)')
#     ax.set_title('Sensitivity Analysis of Olympic Sport Variables')
#     ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
#     ax.grid(True)
#
#     # Add a vertical line at 0% variation
#     ax.axvline(x=0, color='k', linestyle='--')
#
#     plt.tight_layout()
#     plt.show()
#
#
# # Call the function to generate the plot
# visualize_sensitivity()