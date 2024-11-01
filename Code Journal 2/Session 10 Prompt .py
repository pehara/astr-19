# Custom Distribution Histogram: Normal
import numpy as np
import matplotlib.pyplot as plt

random_numbers = np.random.normal(loc=0, scale=1, size=1000)

plt.hist(random_numbers, bins=100, color='lightblue', edgecolor='black')
plt.xlabel("x")
plt.ylabel("N per bin")
plt.title("Normal Distribution Histogram")

plt.savefig("normal_histogram.pdf") 
plt.show()
