# Sine and Cosine Functions
In this notebook, we will define functions to calculate the sine and cosine of a given angle in radians. We will create an array of 1000 evenly spaced values between 0 and 2, then use these functions to compute and display their results.


import math as m
import numpy as np

# Creating an array of 1000 evenly spaced values between 0 and 2
x_values = np.linspace(0, 2, 1000)


## Sine Function
This function takes an input `x` in radians and returns its sine value using the `math.sin()` function.


# Creating a function to calculate sine of x
def sine_function(x):
    """Returns the sine of x (in radians)."""
    return m.sin(x)


## Cosine Function
This function takes an input `x` in radians and returns its cosine value using the `math.cos()` function.


# Creating a function to calculate cosine of x
def cosine_function(x):
    """Returns the cosine of x (in radians)."""
    return m.cos(x)


## Calculating Sine and Cosine Values
In this cell, we compute the sine and cosine values for the previously defined `x` values using the defined functions.


# Calculating the values
s_values = [sine_function(x) for x in x_values]
c_values = [cosine_function(x) for x in x_values]


## Displaying Results
This cell prints the first 10 values of `x`, `sin(x)`, and `cos(x)` in a tabular format for easy viewing.


print(f"{'x':<10}{'sin(x)':<15}{'cos(x)':<15}")

for i in range(10):
    print(f"{x_values[i]:<10.4f}{s_values[i]:<15.4f}{c_values[i]:<15.4f}")



```python

```
