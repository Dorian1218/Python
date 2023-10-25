#calculator app

last10results = []

# function that adds the math equation to the beginning of the list and prints them out
def addsResultToArray(array, result, first_num, second_num, operation):
    if len(array) == 10:
        array.pop()
        array.insert(0, str(first_num) + " " + operation + " " + str(second_num) + " = " + str(result))
    else:
        array.insert(0, str(first_num) + " " + operation + " " + str(second_num) + " = " + str(result))
    print("These are the last 10 results: ")
    for values in array:
        print(values)

#function that checks if a variable is an interger so that only ints can be used as numbers
def checkIfInt(num):
    try:
        num = float(num)
        return True
    except ValueError:
        print("Invalid input. Try Again")
        return False

#function that takes the two numbers, adds them and prints the math equation
def add(first_num, second_num):
    typeNumAgain = True
    while typeNumAgain:
        second_num = input("Choose a second number: ")
        ifInt = checkIfInt(second_num)
        if (ifInt == True):
            typeNumAgain = False
    result = float(first_num) + float(second_num)
    print(str(first_num) + " + " + str(second_num) + " = " + str(result))
    addsResultToArray(last10results, result, first_num, second_num, "+")

#function that takes the two numbers, subtracts them and prints the math equation
def subtract(first_num, second_num):
    typeNumAgain = True
    while typeNumAgain:
        second_num = input("Choose a second number: ")
        ifInt = checkIfInt(second_num)
        if (ifInt == True):
            typeNumAgain = False
    result = float(first_num) - float(second_num)
    print(str(first_num) + " - " + str(second_num) + " = " + str(result))
    addsResultToArray(last10results, result, first_num, second_num, "-")

#function that takes the two numbers, multiplies them and prints the math equation
def multiply(first_num, second_num):
    typeNumAgain = True
    while typeNumAgain:
        second_num = input("Choose a second number: ")
        ifInt = checkIfInt(second_num)
        if (ifInt == True):
            typeNumAgain = False
    result = float(first_num) * float(second_num)
    print(str(first_num) + " * " + str(second_num) + " = " + str(result))
    addsResultToArray(last10results, result, first_num, second_num, "*")

#function that takes the two numbers, divides them and prints the math equation
def divide(first_num, second_num):
    typeNumAgain = True
    while typeNumAgain:
        second_num = input("Choose a second number: ")
        ifInt = checkIfInt(second_num)
        if (ifInt == True):
            typeNumAgain = False
    result = float(first_num) / float(second_num)
    print(str(first_num) + " / " + str(second_num) + " = " + str(result))
    addsResultToArray(last10results, result, first_num, second_num, "/")

# main function where the processes will happen
def main():
    #sets default values for program
    second_number = None
    playAgain = True
    typeOperationAgain = True
    typeNumAgain = True
    print("Welcome to the math calculator\n")
    
    #while loop responsible for rerunning the program when the user types y and ends it when the user types n
    while playAgain:
        while typeNumAgain:
            first_number = input("What is your first number?: ")
            ifInt = checkIfInt(first_number)
            if (ifInt == True):
                typeNumAgain = False
            else:
                continue

        #while loop responsible for rerunning the ask operator when the user types anything other than the 4 operators listed below
        while typeOperationAgain:
            operator = input("What operator do you want to use? \n + for addition \n - for subtraction\n * for multiplication \n / for division \n: ")
            # switch case that will take the input of the user and assign a function depending on it
            match operator:
                case "+":
                    typeOperationAgain = False
                    add(first_number, second_number)
                case "-":
                    typeOperationAgain = False
                    subtract(first_number, second_number)
                case "*":
                    typeOperationAgain = False
                    multiply(first_number, second_number)
                case "/": 
                    typeOperationAgain = False
                    divide(first_number, second_number)
                case _:
                    print("Your input is not one of the avaliable operations")

        userResponse = input("Do you want to play again: y/n: ")

        #checks if the user typed a y or n to rerun the program
        if userResponse[0].lower() == "y":
            typeOperationAgain = True
            typeNumAgain = True
            continue
        elif userResponse[0].lower() == "n":
            playAgain = False

main()