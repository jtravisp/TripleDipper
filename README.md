# Triple Dipper Combinations Calculator

This Python script calculates the total number of possible combinations for the **Triple Dipper** menu item at the Chili's at 45th and Lamar, considering various selection criteria, including options for wings and dipping sauces. It also calculates how long it would take to try every combination if you visited the Chili's at 45th and Lamar daily.

## Purpose

The script explores the combinatorial possibilities of creating a Triple Dipper order from:

1. **9 main food items**, chosen 3 at a time, with repetition allowed.
2. **10 delicious wing sauces**, applied to wing items if selected (boneless or bone-in).
3. **15 Chili's exclusive dipping sauces**, chosen 3 at a time, with repetition allowed.

The calculations include:

- Base combinations without wing sauces.
- Combinations factoring in wing sauces.
- Combinations factoring in both wing sauces and dipping sauces.

Finally, the script displays the number of combinations, how long it would take to try each combination (in years and days).

While the "best combination" is beyond the scope of this project and widley considered to be subjective, anecdotal evidence strongly suggest the best combination (sauce choices excluded) is:

- Southwestern Egg Rolls
- Big Mouth Bites
- Honey Chipotle Chicken Crispers

## Selection Criteria

1. **Food Options**:
   - You select 3 items from a list of 9, allowing repetition.
   - Options include Fried Mozzarella, Nashville Hot Mozz, Southwestern Egg Rolls, Bone-In Wings, Boneless Wings, Big Mouth Bites, Crispy Chicken Crispers, Honey Chipotle Chicken Crispers, and Nashville Hot Chicken Crispers.

2. **Wing Sauces**:
   - If you choose wings (boneless or bone-in), you must select one of 10 wing sauces for each wing item.
   - The sauces include options like Garlic Parmesan, Buffalo, and Mango Habanero.

3. **Dipping Sauces**:
   - You also choose 3 dipping sauces from a list of 15, allowing repetition.
   - Dipping sauces are exclusive to Chili's and add flavor variety.

## Features

**Combination Calculation**:

- Computes combinations with and without wing sauces and dipping sauces.
- Outputs results with formatted numbers for readability.
  
**Time Estimation**:

- Converts the total number of combinations into the time it would take to try them all (in years and days).

## Example Output

```

🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️
The total number of possible combinations for the Triple Dipper at the Chili's at 45th and Lamar without considering wing or dipping sauces is: 729
It would take 1 year and 364 days to try every combination without considering wing sauces.

The total number of possible combinations for the Triple Dipper at the Chili's at 45th and Lamar, including 10 delicious wing sauce options, is: 3,439
It would take 9 years and 154 days to try every combination including wing sauces.

The total number of possible combinations for the Triple Dipper at the Chili's at 45th and Lamar, including those irresistible wing sauces and 15 Chili's exclusive dipping sauces, is: 11,606,625
It would take 31,798 years and 355 days to try every combination including wing sauces and dipping sauces.
🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️    🌶️

```
