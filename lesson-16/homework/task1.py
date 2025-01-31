import numpy as np

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

# Vectorize the function
vectorized_converter = np.vectorize(fahrenheit_to_celsius)

# Array of temperatures in Fahrenheit
fahrenheit_temps = np.array([32, 68, 100, 212, 77])

# Convert to Celsius
celsius_temps = vectorized_converter(fahrenheit_temps)
print("Temperatures in Celsius:", celsius_temps)