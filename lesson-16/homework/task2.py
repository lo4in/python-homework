import numpy as np


# Custom function to calculate power
def power_function(number, power):
    return number**power

# Vectorize the function
vectorized_power = np.vectorize(power_function)

# Arrays of numbers and powers
numbers = np.array([2, 3, 4, 5])
powers = np.array([1, 2, 3, 4])

# Calculate powers
result = vectorized_power(numbers, powers)
print("Power results:", result)