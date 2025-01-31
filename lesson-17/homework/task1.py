import matplotlib.pyplot as plt
import numpy as np

# Define the function
x = np.linspace(-10, 10, 400)
y = x**2 - 4*x + 4

# Plot the function
plt.plot(x, y, label="$f(x) = x^2 - 4x + 4$")
plt.title("Plot of $f(x) = x^2 - 4x + 4$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()