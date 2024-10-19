# Python script that print out the first 10 values of x, sin(x), and cos(x) in columns.

import math as m
import numpy as np

# creating an array of 1000 evenly spaced values between 0 & 2
x_values = np.linspace(0, 2, 1000)

# creating a function to calculate sine of x
def sine_function(x):
    """Returns the sine of x (in radians)."""
    return m.sin(x)

# creating a function to calculate cosine of x
def cosine_function(x):
    """Returns the cosine of x (in radians)."""
    return m.cos(x)

# calculating the values
s_values = [sine_function(x) for x in x_values]
c_values = [cosine_function(x) for x in x_values]

print(f"{'x':<10}{'sin(x)':<15}{'cos(x)':<15}")

for i in range(10):
    print(f"{x_values[i]:<10.4f}{s_values[i]:<15.4f}{c_values[i]:<15.4f}")