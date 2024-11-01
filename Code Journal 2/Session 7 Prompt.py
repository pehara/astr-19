# Exponential Plot
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

def exponential(x):
    return np.exp(x)

y = exponential(x)


plt.plot(x, y)
plt.xlabel("Time [milliseconds]")
plt.ylabel("Awesomeness")
plt.title("Exponential Growth")

plt.savefig("exponential_plot.pdf") 
plt.show()
