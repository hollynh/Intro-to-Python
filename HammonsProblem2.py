### STEP ONE: PUPOSE OF THE CODE
   # The user will input the cost of a new car, estimated miles driven per year,
   # the estimated gas price, fuel efficiency, and estimated resale value.
   # The code will tell the user how much the car will cost them, if they sell
   # it in five years.


### STEP TWO: HAND EXAMPLES OF CALCULATION
    # cost of gas = (miles driven per year/efficiency) * cost of gas * 5 (years)
    # Total spent on the car = cost of the new car - resale value
    # cost of electric car after 5 years = 35000*.8


### STEP THREE: WRITE THE PSEUDOCODE
   # Call the main function
   # User inputs the cost of the new car
   # User inputs the estimated miles driven per year
   # User inputs estimated gas price
   # User inputs efficiency in miles per gallon
   # User inputs estimated resale value after 5 years
   # Gas is calculated using cost of gas equation
   # total spent on car is calculated using total spent on the car equation
   # cost of electric car is calculated using cost of electric car after 5 years equation
   # print the cost of gas over five years, the cost of the car, and then
   # the total spent in five years. Compare it to the cost of a $35,000 electric car.


### STEP FOUR: DETERMINE THE INPUT VALUE
    # Floats
    # Variable names: newCar, mileYear, costGas, mpgCar, resaleVal
    # The type is: Float
    # The range is: Any number


### STEP 5: DETERMINE THE OUTPUT
   # String, Float
   # It will output a string that explains how much the car will cost in five
   # years. It will compare it to the cost of an electric car
   # It will output the variables: fiveGas, carCost, and totalCost, and elecSell


### STEP 6: THE CODE

#******************************************************************************
# Program Name:     Cost of New Car After Five Years
# Programmer:       Holly Hammons
# Date of Program:  03/04/2020
# Purpose:          To determine the cost of a car after five years
# Modules Used:     None
# Input Variables:  Floats
# Output:           Strings, floats
#******************************************************************************


def main(): # calling the main function

    # Enters input values in floats
    newCar = float(input("Enter the cost of a new car:")) 
    mileYear = float(input("Enter the amount of miles driven per year:"))
    costGas = float(input("Enter the estimated cost of gas:"))
    mpgCar = float(input("Enter the fuel efficiency in mpg:"))
    resaleVal = float(input("Enter the estimated resale value of car after 5 years:"))

    # calculates the cost of gas and ownership for 5 years
    calcGas = (mileYear / mpgCar) *costGas
    fiveGas = 5 * calcGas
    carCost = newCar - resaleVal
    totalCost = fiveGas + carCost
    
    # calculates the cost of electric car assuming resale value is 80% of original
    elecCar = 35000.0
    elecSell = (35000.0 * .2)

    # prints a statement explaining the cost after 5 years, this also compares
    # it to the cost of an electric car after selling it as well.
    print("It will cost you $", fiveGas, " in gas for five years. If you sell \n"
          + " the car in five years, the total cost spent on the car will be $", carCost, ". \n"
          + " The total cost spent on the car and gas in five years is $", totalCost, "The \n"
          + "average cost of an electric car is $35,000. Assuming the resale value \n"
          + " is 80% of the original cost in five years, an electric car would cost \n"
          + "you", elecSell)

if __name__== '__main__': 
      main() # calls the main function
      

### STEP 7: SHOW THE OUTPUT OF YOUR TESTS
      # Enter the cost of a new car:25000
      # Enter the amount of miles driven per year:1000
      # Enter the estimated cost of gas:2.8
      # Enter the fuel efficiency in mpg:20
      # Enter the estimated resale value of car after 5 years:10000
      # It will cost you $ 700.0  in gas for five years. If you sell
      # the car in five years, the total cost spent on the car will be $ 15000.0 .
      # The total cost spent on the car and gas in five years is $ 15700.0 The
      # average cost of an electric car is $35,000. Assuming the resale value
      # is 80% of the original cost in five years, an electric car would cost
      # you 7000.0
      # >>> 


