def compundYearly(interest, years, principle): # compound interest function
    import math
    totalBalance = principle * (pow((1+interest/100),years))
    return totalBalance

def testFunction(): # unit test function
    import math
    interest = 99
    years = 0
    principle = 1
    result = compundYearly(interest, years, principle)
    if result == 1:
        return True # returns True if function works
    else:
        exit
        
def isFloat(x, y, z): # function to validate user input
    try:
        float(x)
        float(y)
        float(z)
        return True # if each parameter can be converted to a float, return True
    except ValueError:
        return False
    
def main(): # defines the main function
    while True: # this first loop is for restarting the program
        while True: # this second loop is to validate the user input
            interestRate = input("What is the interest rate at your bank?")
            balanceTerm = input("How long will you leave your money in the bank?")
            ogBalance = input("How much money are you Depositing?")
            if isFloat(interestRate, balanceTerm, ogBalance): # if each parameter can be converted to a float, convert all inputs to floats
                fInterestRate = float(interestRate)
                fBalanceTerm = float(balanceTerm)
                fOgBalance = float(ogBalance)
                break
            else: # if any of the parameters can't be converted to a float, start the loop over and enter inputs again
                print("incorrect input, please enter a number again")
                continue
        testResult = testFunction()
        if testResult: # if the test function works properly, send new parameters through the compound interest function
            result = compundYearly(fInterestRate, fBalanceTerm, fOgBalance)
            print("After ", balanceTerm, "years your total balances will be $",\
              result, "at an interest rate of ", interestRate) # prints result
            keepGo = input(("Would you like to try again? Y or N:")) # asks user to restart
            if keepGo == "Y" or keepGo == "y":
                continue # restarts loop for Y or y
            else: 
                break # ends the program for anything else
    else:
        print("The compound interest function is broken, don't use this program") # tells the user that the function is broken
if __name__== '__main__':   
    main() 
