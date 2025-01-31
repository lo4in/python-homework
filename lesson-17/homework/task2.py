import matplotlib.pyplot as plt
import numpy as np

# Define x values
x = np.linspace(0, 2*np.pi, 400)

# Plot sin(x) and cos(x)
plt.plot(x, np.sin(x), label="$\sin(x)$", linestyle="--", marker="o", color="blue", markersize=5)
plt.plot(x, np.cos(x), label="$\cos(x)$", linestyle=":", marker="s", color="red", markersize=5)
plt.title("Sine and Cosine Functions")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()