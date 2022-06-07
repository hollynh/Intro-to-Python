# positive, negative, or zero number. Print small and large.

num = float(input("Please enter any number:")) # float input, named num
if num < -0.00000000000000000001: # negative number
    print("Your number is negative.")
elif num > 0.00000000000000000001: # positive number
    print("Your number is positive.")
elif num < 0.00000000000000000001 or num > 0.00000000000000000001: # must use two side equality for 0
    print("Your number is zero.")
absNum = abs(num) # naming absolute value variable
if absNum < 0.999999999999999999: # for small number
    print("small number")
elif absNum > 1000000.0000000000000000000000001: # for large number
    print("large number")
