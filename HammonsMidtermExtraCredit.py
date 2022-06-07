# You must have completed and turned in
# all previous questions to get points on this one.
# This problem is worth an additional 15 points for the coding portion


#Correct Syntax & logic errors - 5 points
#Add a main function - 2.5 points
#Add comments to the code (to explain what it is doing) - 2.5
#Add a retry loop (prompt user to start over) -5 points

def main(): # calls the main function

    while True:
        x = float(input("Enter a number as a float:")) # user inputs a number
        y = float(input("Enter a second number as a float:")) # user inputs a second number

        if x == y: 
            print("You entered the same numbers!") # prints if the two numbers are the same
        elif x < y: 
            print("The first number is smaller") # prints if the first number is smaller than the second number
        else:
            print("The first number is larger") # prints if the first number is larger than the second number

        if -0.01 < x - y and x - y < 0.01:
            print("The numbers are close together") # prints if the difference between the numbers is within .01
        if x > 0 and y > 0 or x < 0 and y < 0:
            print("The numbers have the same sign") # prints if the numbers are both negative or both positive
        else:
            print("The numbers have different signs")

        restart = input("Would you like to restart? Y or N:") # prompts to restart the program
        if restart == "Y" or restart == "y":
            continue # starts the program over
        else:
            break # stops the program
        
if __name__== '__main__': 
      main()
