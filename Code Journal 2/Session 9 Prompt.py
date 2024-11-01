# Uniform Distribution Histogram
import numpy as np
import matplotlib.pyplot as plt

random_numbers = np.random.uniform(0, 1, 1000)

plt.hist(random_numbers, bins=100, color='pink', edgecolor='black')
plt.xlabel("x")
plt.ylabel("N per bin")
plt.title("Uniform Distribution Histogram")

plt.savefig("uniform_histogram.pdf")  
plt.show()
