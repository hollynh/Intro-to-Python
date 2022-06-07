### STEP ONE: PUPOSE OF THE CODE
    # The program will collect user information. It will ask them what their
    # favorite food is, what their favorite whole numbers are, and what
    # their favorite numbers are of any kind. It will tell how many uppercase
    # and digits are in their favorite food, the smallest, largest, and average
    # of their favorite whole numbers, and the average and range of their
    # favorite numbers of any kind.


### STEP TWO: HAND EXAMPLES OF CALCULATION
    # When a string is entered for favorite food, the number of uppercase letters
    # will be printed. The len() funtion is then used to tell the total number
    # of characters. Next, the three user int inputs will be evaluated for min,
    # max, and average values. The average is calculated from adding all of the
    # values up, and then dividing by the length of the list. Next, the average
    # and range will be calculated from the float inputs. The average is done
    # the same as before, while the range is calculated from subtracting the max
    # value from the min value.


### STEP THREE: WRITE THE PSEUDOCODE
    # 1. def main():
    # 2. "This program will collect user info"
    # 3. restart == "Y", while restart == "Y"
    # 4. favFood = input("What is your favorite food?")
    # 5. uses for loop with a counter. for i in loop, it counts the number
    # of uppercase letters with the .isupper() function
    # 6. uses len() to find total characters
    # prints length and number of uppercase letters
    # 7. numbersIn = []
            #currentValue = 0
            #stopValue = 2
            #while currentValue <= stopValue:
                  #currentValue = currentValue +1
    # uses another loop to ensure 3 inputs, with [] as an empty list to collect
    # the user input
    # 8. uses max and min functions for user input
    # 9. takes the average
    # 10. prints max, min, and average
    # 11. newNums = []
            #addMore = "Y"
            #while addMore == "Y" or "y":
                  #newNumIn = input("Enter any favorite number:")
                  #newNums.append(float(newNumIn))
                  #addMore = input("Would you like to enter another number? Y or N:")
                  #if addMore == "Y":
                        #continue
                  #elif addMore == "N":
                        #break
                  #else:
                        #print("You entered an invalid input, the program will be redirected to input again:")
                        #continue
    # uses the same method as before, but this time asks to continue after each
    # input. Here, the user can choose how many numbers are entered.
    # 12. uses max and min functions for user input
    # 13. calculates the average and the range
    # 14. restart = input("Would you like to restart the program? Y or N:")
            #if restart == "Y":
                  #main()
            #else:
                  #break
            #break
    # This can either restart or terminate the program.
    # 15. if __name__== '__main__':
      #main()
    # This will call the main function from the beginning


### STEP FOUR: DETERMINE THE INPUT VALUE
    # The input values for this code are strings, integers, and floats
    # Variable name: restart, favFood, numUpper, numbersIn, currentValue,
    # stopValue, numIn, maxNum, minNum, aveNum, newNums, addMore, newNumIn,
    # aveNewNum, minNewNum, maxNewNum, theRange
    # The type is: int, str, float
    # The range is all letters, Y, N, all whole numbers, and all real numbers


### STEP 5: DETERMINE THE OUTPUT
    # The output will be a string that says "The number of uppercase letters in your
    # favorite food are", "The total number of letters in your favorite food are:",
    # "what is your favorite food", "please enter a favorite whole number",
    # "the smallest, largest, and average of the whole numbers entered is",
    # "enter any favorite number", "would you like to enter another number Y or N"
    # "You entered an invalid input, the program will be redirected to input again:"
    # "The average and range of your numbers are"
    # ""Thank you for allowing this program to collect your information. Your favorite food is: favFood. Your favorite whole numbers
    # are: numbersIn, and your favorite numbers of any kind are: newNums.
    # "Would you like to restart the program? Y or N:"


### STEP 6: THE CODE

#******************************************************************************
# Program Name:     Collect User Information
# Programmer:       Holly Hammons
# Date of Program:  February 23, 2020
# Purpose:          To collect user information
# Modules Used:     None
# Input Variables:  Strings, integers, floats
# Output:           Strings, integers, floats
#******************************************************************************




def main():
      print("This program will collect user information.")
      restart = "Y"
      while restart == "Y":
            favFood = input("What is your favorite food?")
            numUpper = 0
            for i in favFood:
                  if(i.isupper()):
                        numUpper = numUpper + 1
            favTotal = len(favFood)
            print("The number of uppercase letters in your favorite food are:", numUpper)
            print("The total number of letters in your favorite food are:", favTotal)



            numbersIn = []
            currentValue = 0
            stopValue = 2
            while currentValue <= stopValue:
                  currentValue = currentValue +1
                  numIn = int(input("Please enter a favorite whole number:"))
                  numbersIn.append(numIn)
                  continue
            maxNum = max(numbersIn)
            minNum = min(numbersIn)
            aveNum = (sum(numbersIn))//(len(numbersIn))
            print("The largerst number entered is:", maxNum)
            print("The smallest number entered is:", minNum)
            print("The average of your numbers are:", aveNum)


            newNums = []
            addMore = "Y"
            while addMore == "Y" or "y":
                  newNumIn = input("Enter any favorite number:")
                  newNums.append(float(newNumIn))
                  addMore = input("Would you like to enter another number? Y or N:")
                  if addMore == "Y":
                        continue
                  elif addMore == "N":
                        break
                  else:
                        print("You entered an invalid input, the program will be redirected to input again:")
                        continue
            aveNewNum = (sum(newNums))/(len(newNums))
            print("The average of your numbers are:", aveNewNum)
            maxNewNum = max(newNums)
            minNewNum = min(newNums)
            theRange = maxNewNum - minNewNum
            print("The range of your numbers are:", theRange)
            print("Thank you for allowing this program to collect your information. \n"
                  + "Your favorite food is:", favFood, ". Your favorite whole numbers \n"
                  + " are:", numbersIn, " and your favorite numbers of any kind are:", newNums)
            restart = input("Would you like to restart the program? Y or N:")
            if restart == "Y":
                  main()
            else:
                  break
            break
if __name__== '__main__':
      main()

### STEP 7: SHOW THE OUTPUT OF YOUR TESTS
# This program will collect user information.
# What is your favorite food?SalAd
# The number of uppercase letters in your favorite food are: 2
# The total number of letters in your favorite food are: 5
# Please enter a favorite whole number:33
# Please enter a favorite whole number:23
# Please enter a favorite whole number:5
# The largerst number entered is: 33
# The smallest number entered is: 5
# The average of your numbers are: 20
# Enter any favorite number:2.67
# Would you like to enter another number? Y or N:Y
# Enter any favorite number:3.4
# Would you like to enter another number? Y or N:Y
# Enter any favorite number:4.5
# Would you like to enter another number? Y or N:N
# The average of your numbers are: 3.5233333333333334
# The range of your numbers are: 1.83
# Thank you for allowing this program to collect your information. 
# Your favorite food is: SalAd . Your favorite whole numbers 
#  are: [33, 23, 5]  and your favorite numbers of any kind are: [2.67, 3.4, 4.5]
# Would you like to restart the program? Y or N:Y
# This program will collect user information.
# What is your favorite food?BurgERs
# The number of uppercase letters in your favorite food are: 3
# The total number of letters in your favorite food are: 7
# Please enter a favorite whole number:12
# Please enter a favorite whole number:98
# Please enter a favorite whole number:4
# The largerst number entered is: 98
# The smallest number entered is: 4
# The average of your numbers are: 38
# Enter any favorite number:8.7
# Would you like to enter another number? Y or N:Y
# Enter any favorite number:4
# Would you like to enter another number? Y or N:df
# You entered an invalid input, the program will be redirected to input again:
# Enter any favorite number:3.4
# Would you like to enter another number? Y or N:Y
# Enter any favorite number:2
# Would you like to enter another number? Y or N:N
# The average of your numbers are: 4.5249999999999995
# The range of your numbers are: 6.699999999999999
# Thank you for allowing this program to collect your information. 
# Your favorite food is: BurgERs . Your favorite whole numbers 
#  are: [12, 98, 4]  and your favorite numbers of any kind are: [8.7, 4.0, 3.4, 2.0]
# Would you like to restart the program? Y or N:N
# >>> 
   


      





