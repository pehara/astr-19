# Sine and Cosine Multipanel Plot
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 1, 100)

y_sin = np.sin(x)
y_cos = np.cos(x)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.plot(x, y_sin)
ax1.set_title("sin(x)")
ax1.set_xlabel("x")
ax1.set_ylabel("sin(x)")

ax2.plot(x, y_cos)
ax2.set_title("cos(x)")
ax2.set_xlabel("x")
ax2.set_ylabel("cos(x)")

plt.savefig("sine_cosine_multipanel.pdf")
plt.show()
