# Hello Variable World Activity

# Formulas Needed:
# abs_return = Current Price - Original Price
# Percent abs_return = abs_return / Original x 100

# Create float variable for original_price
original_price = 198.87

# Create float variable for current_price
current_price = 254.32

# Calculate difference between current_price and original_price
abs_return = current_price - original_price

# Calculate percent abs_return
percent_abs_return = (abs_return / original_price) * 100

# Print original_price
print(f"Apple's original stock price was ${original_price}")

# Print current_price
print(f"Apple's current stock price is ${current_price}")

# Print percent abs_return
print(f"Apple's stock price abs_return by ${abs_return}")

# CHALLENGE:
# Use a format specifier with the f-string to print the percent abs_return with two decimal places:
print(f"Apples percent abs_return in price is {percent_abs_return:.2f}%")