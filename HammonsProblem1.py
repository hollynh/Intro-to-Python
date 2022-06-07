def main(): # calls the main function
    
    while True: # first boolean to ensure the program can restart
        inList = [] # empty list to store users input values
        moreNum = "Y" # naming this variable before the while loop
        while moreNum == "Y" or moreNum == "y": # loop for adding as many number as the user wants
            inNum = float(input("Enter any number:"))
            inList.append(inNum) # adds numbers to inList
            moreNum = input("Any more numbers? Y or N:")
            if moreNum == "Y" or moreNum == "y":
                continue # restarts the loop if user wants to input new numbers
            else:
                break # stops the loop
        minInt = min(inList) # finds the minimum value from the list
        print("The smallest number entered was:", minInt)

        restart = input("Would you like to restart the program? Y or N:") # names variable to restart the program
        if restart == "Y" or restart == "y":
            continue # loops back to the "while True" loop
        else:
            break # ends the program

if __name__== '__main__': 
      main() # calls the main function
