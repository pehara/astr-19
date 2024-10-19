# Python script that returns the value of X and checks to see if it is above 27.

def f(x):
    result = x**3 + 8
    print ("the result is: ", result)
    if result > 27:
         print("YAY!")
    else:
        return

f(9)