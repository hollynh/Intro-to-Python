# calling the main function
def main():

    numOne = float(input("Enter any favorite number:")) # inputs a number
    while True: # restarts here if number is invalid
        numTwo = float(input("Enter a favorite number greater than 30:"))
        if numTwo > 30:
            break # brakes out of the loop if its valid
        else: # number needs to be greater than 30
            print("You entered an invalid number, please enter again")
            continue # restarts loop if number is less than 30        
        
    # input strings
    foodIn = input("Enter your favorite food:")
    drinkIn = input("What is your favorite drink?")
    
    foodUpper = foodIn.upper() # changes the string inputs to uppercase

    print(" \t Your first favorite number that you entered is", numOne, ".\n"
          + " The second favorite number entered was", numTwo, ". Your favorite \n"
          + "food in uppercase is", foodUpper, ". Your favorite drink is", drinkIn,".")    

if __name__== '__main__': 
      main() # calls the main function
