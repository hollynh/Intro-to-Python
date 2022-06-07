### STEP ONE: PUPOSE OF THE CODE
    # Program will ask user for their lucky number. It will then rspond with
    # a statement saying the number is small, large, or very large.


### STEP TWO: HAND EXAMPLES OF CALCULATION
    # If the user enters a number <=10, the code should say it's small
    # If the user enters a number >10 and <100, the code should say it's large
    # If the user enters any other number, the code should say it's very large


### STEP THREE: WRITE THE PSEUDOCODE
    # 1. while True (must start loop in beginning)
    # 2. luckyNumber = int(input("What is your lucky number?"))
    # 3. if statement for number <= 10
    # 4. elif statement for >10 and <100
    # 5. else statement for other numbers
    # 6. keepGoing = input("Would you like to start over? Answer Y or N:")
    # 7. if statement for no, break (stops program)
    # 8. elif statement for yes, continue (restarts program)
    # 9. else statement for anything else, says invalid, break


### STEP FOUR: DETERMINE THE INPUT VALUE
    # The input value for this code is an integer, and 'Y' 'y' 'N' 'n'
    # Variable name: luckyNumber, keepGoing
    # The type is: int, str
    # The range is all real integers, Y, y, N, n


### STEP 5: DETERMINE THE OUTPUT
    # The output will be a string that says "Your lucky number is small, large,
    # or very large."
    # It will then start over or terminate the program


### STEP 6: THE CODE

#******************************************************************************
# Program Name:     Lucky Number
# Programmer:       Holly Hammons
# Date of Program:  February 13, 2020
# Purpose:          To determine if a lucky num is small, large, or very large
# Modules Used:     None
# Input Variables:   Any integer, Y and N
# Output:           "Your lucky number is small, large, or very large" Restart
#                   or stop.
#******************************************************************************


while True:
    luckyNumber = int(input("What is your lucky number?"))

    if luckyNumber <= 10:
        print("Your lucky number is a small number!")
    elif luckyNumber > 10 and luckyNumber < 100:
        print("Your lucky number is a large number!")
    else:
        print("Your lucky number must be very large!")
    keepGoing = input("Would you like to start over? Answer Y or N:")

    if keepGoing == 'Y' or keepGoing == 'y':
        continue 
    elif keepGoing == 'N' or keepGoing == 'n':
        print("Okay, goodbye.")
        break
    else:
        print("Invalid input, the program will end now.")
        break


### STEP 7: SHOW THE OUTPUT OF YOUR TESTS
   # What is your lucky number?9
   # Your lucky number is a small number!
   # Would you like to start over? Answer Y or N:Y
   # What is your lucky number?59
   # Your lucky number is a large number!
   # Would you like to start over? Answer Y or N:Y
   # What is your lucky number?123
   # Your lucky number must be very large!
   # Would you like to start over? Answer Y or N:N
   # Okay, goodbye.
   #
   # What is your lucky number?12
   # Your lucky number is a large number!
   # Would you like to start over? Answer Y or N:drg
   # Invalid input, the program will end now.
   
