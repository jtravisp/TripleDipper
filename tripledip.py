num_food_items = 9  # Total food options
num_choices = 3  # Number of food items chosen
num_wing_sauce_options = 10  # Wing sauces
num_dipping_sauces = 15  # Total dipping sauces
num_sauce_choices = 3  # Number of dipping sauces chosen

# Total combinations without considering wing sauces
base_combinations = num_food_items ** num_choices

# Add combinations for wing sauces
total_combinations = 0

for wings in range(4):  # 0, 1, 2, or 3 wings
    non_wing_items = num_choices - wings  # Remaining choices for non-wing items
    if non_wing_items < 0:
        continue  # Skip invalid combinations

    # Calculate combinations for this configuration
    wing_sauce_combinations = (num_wing_sauce_options ** wings)
    non_wing_combinations = (num_food_items ** non_wing_items)

    # Add to total combinations
    total_combinations += wing_sauce_combinations * non_wing_combinations

# Dipping sauces combinations
dipping_sauce_combinations = num_dipping_sauces ** num_sauce_choices

# Final total combinations including dipping sauces
final_combinations = total_combinations * dipping_sauce_combinations

# Function to convert days into years and remaining days
def days_to_years_and_days(days):
    years = days // 365  # Full years
    remaining_days = days % 365  # Remaining days
    return years, remaining_days

# Calculate years and days for each case
base_years, base_days = days_to_years_and_days(base_combinations)
total_years, total_days = days_to_years_and_days(total_combinations)
final_years, final_days = days_to_years_and_days(final_combinations)

def prGreen(skk): print("\033[92m{}\033[00m" .format(skk))
chili_count = 24

print("\n")
print("".join(["🌶️    " for _ in range(chili_count)]).strip() + "")
print(f"The total number of possible combinations for the Triple Dipper at the Chili's at 45th and Lamar without considering wing or dipping sauces is: {base_combinations}")
if base_years == 1:
    prGreen(f"It would take {base_years} year and {base_days} days to try every combination without considering wing sauces.\n")
else:
    prGreen(f"It would take {base_years} years and {base_days} days to try every combination without considering wing sauces.\n")

print(f"The total number of possible combinations for the Triple Dipper at the Chili's at 45th and Lamar, including 10 delicious wing sauce options, is: {total_combinations:,}")
prGreen(f"It would take {total_years} years and {total_days} days to try every combination including wing sauces.\n")

print(f"The total number of possible combinations for the Triple Dipper at the Chili's at 45th and Lamar, including those irresistible wing sauces and 15 Chili's exclusive dipping sauces, is: {final_combinations:,}")
prGreen(f"It would take {final_years:,} years and {final_days} days to try every combination including wing sauces and dipping sauces.")

print("".join(["🌶️    " for _ in range(chili_count)]).strip() + "\n")

