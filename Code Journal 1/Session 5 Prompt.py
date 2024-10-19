# Python script that writes out a table of the function sin(x) vs. x.

import math

def main():
    for i in range(1001):
        x = i * (2/1000)
        print(f"x: {x:.3f}, sin(x): {math.sin(x):.3f}")
        
main()