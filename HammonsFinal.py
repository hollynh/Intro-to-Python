import math
def grades(x, y): # finds the sum of the two grades
    gradeSum = x + y
    return gradeSum
def average(x, y): # finds the average of the two grades
    averageGrade = (x + y) / 2
    return averageGrade
def studentGPA(x, y, z): # calculates the GPA based on the two grades
    if (x + y)/2 >= 90.0: 
        weight = 4.0
        GPA = (weight * z)/z
        return GPA
    elif (x + y)/2 >= 80.0 and (x + y)/2 < 90:
        weight = 3.0
        GPA = (weight * z)/z
        return GPA
    elif (x + y)/2 >= 70.0 and (x + y)/2 < 80:
        weight = 2.0
        GPA = (weight * z)/z
        return GPA
    elif (x + y)/2 >= 60.0 and (x + y)/2 < 70:
        weight = 1.0
        GPA = (weight * z)/z
        return GPA
    else:
        weight = 0.0
        GPA = (weight * z)/z
        return GPA
def letterGrade(x, y): # calculates the letter grade based on the two grades
    if (x + y)/2 >= 90.0:
        letter = "A"
        return letter
    elif (x + y)/2 >= 80.0 and (x + y)/2 < 90:
        letter = "B"
        return letter
    elif (x + y)/2 >= 70.0 and (x + y)/2 < 80:
        letter = "C"
        return letter
    elif (x + y)/2 >= 60.0 and (x + y)/2 < 70:
        letter = "D"
        return letter
    else:
        letter = "F"
        return letter
def unitTest(): # unit test to test for the sum of the grades calculation
    x = 50.0
    y = 49.0
    result = grades(x, y)
    if result == 99.0:
        return True # if the unit test works
    else: # if it's false
        exit
def rangeIn(n): # user validation for test score range between 0-100
    if n >= 0.0 and n <= 100.0:
        return True
    else:
        return False
def isFloat(n): # user validation for float input
    try:
        float(n)
        return True
    except ValueError: # if it's a string
        return False
    
# main function
def main():
    while True: # loop for restarting the program
        listIn = [] # empty list to store variables for lines
        fileIn = open("studentExams.txt", "r")
        for line in fileIn:
            listIn.append(line.strip()) # add items to the list
        fileIn.close() # close in file
        lineOne = listIn[0] # names first line as variable
        lineTwo = listIn[1] # names second line as variable
        nameStudent = input("Enter your name:")
        nameClass = input("Enter the name of the class:")
        newGrades = [] # empty list to store grades
        while True: # loop for user-validation
            # I'm using test values between 1-100, bacuase tests usually aren't scored by 50
            scoreMid = input("Enter the grade received on the {} (between 0-100):".format(lineOne)) # using variable from file
            if isFloat(scoreMid): # user float validation
                scoreMid = float(scoreMid)
                if rangeIn(scoreMid) == False: # user range validation
                    print("Out of range, enter again")
                    continue
                else:
                    newGrades.append(scoreMid)
                    break # end loop
            else:
                print("Invlid input, please try again.")
                continue # user validation failed
        while True: # loop for user-validation
            # I'm using test values between 1-100, bacuase tests usually aren't scored by 50
            scoreFinal = input("Enter the grade received on the {} (between 0-100):".format(lineTwo))
            if isFloat(scoreFinal): # user float validation
                scoreFinal = float(scoreFinal)
                if rangeIn(scoreFinal) == False: # user range validation
                    print("Out of range, enter again")
                    continue
                else:
                    newGrades.append(scoreFinal)
                    break # end loop
            else:
                print("Invlid input, please try again.")
                continue # user validation failed
        testResult = unitTest() # checks unit test
        if testResult: # if unit test works
            sumGrade = grades(newGrades[0], newGrades[1])
            sSumGrade = str(sumGrade) # converts to string to write to file
            aveGrade = average(newGrades[0], newGrades[1])
            sAveGrade = str(aveGrade) # converts to string to write to file
            studGpa = studentGPA(newGrades[0], newGrades[1], 3.0)
            sStudGpa = str(studGpa) # converts to string to write to file
            letGrade = letterGrade(newGrades[0], newGrades[1])
            fileName = nameStudent + ".txt" # for use in writing a file and printing in console

            outfile = open(fileName, "w") # creating outfile
            outfile.write("Name:" + nameStudent + "\n") # writing to file
            outfile.write("Class:" + nameClass + "\n") # writing to file
            outfile.write("Average Grade:" + sAveGrade + "\n") # writing to file
            outfile.write("Sum of Grades:" + sSumGrade + "\n") # writing to file
            outfile.write("GPA:" + sStudGpa + "\n") # writing to file
            outfile.write("Letter Grade:" + letGrade + "\n") # writing to file
            outfile.close() # close out file

            print("The student", nameStudent, "recieved a", letGrade, "in", nameClass, "and has a GPA of", studGpa, "\n"
                + "For further info on this student you may review the file", fileName)

            
            ecDictionary = {"Student Name":nameStudent, "Class":nameClass, "Average Grade":aveGrade, "Letter Grade":letGrade, "GPA":studGpa}
            print(ecDictionary) # extra credit dictionary
            
            keepGo = input(("Would you like to try again? Y or N:")) # asks user to restart
            if keepGo == "Y" or keepGo == "y":
                continue # restarts loop for Y or y
            else: 
                break # ends the program for anything else
        else:
            print("The compound interest function is broken, don't use this program") # tells the user that the function is broken
    
# calls the main function        
if __name__== '__main__':   
    main()
