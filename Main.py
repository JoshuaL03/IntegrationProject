"""Basic Calculator Program"""
__author__ = "Joshua Lopez"


# This program is meant to function as a basic calculator
# that can perform the four basic mathematical operations
# as well as exponentiation, modular division, and floor division.
# It additionally compares the last two answers.

# Numeric operators
# The + operator signifies addition.
# The - operator signifies subtraction.
# The * operator signifies multiplication.
# The / operator signifies division.
# The ** operator signifies exponentiation.
# The % operator signifies modular division (take remainder from a quotient).
# The // operator signifies floor division (round quotient down to integer).

# String operators
# The + operator signifies addition/concatenation of a string (combines them).
# The * operator signifies multiplication of a string (repeats it x times).

# Shortcut operators
# The += operator signifies addition of a variable with some x.
# The -= operator signifies subtraction of some x from a variable.
# The *= operator signifies multiplication of a variable by some x.
# The /= operator signifies division of a variable by some x.


def print_welcome():
    """The function gives a basic description of the program upon startup."""
    print("\nHello! This is a simple calculator.")
    print("It can perform addition, subtraction, multiplication, division,"
          "\nexponentiation, modular division, and floor division.")


def print_ending(num_calculation):
    """The function provides an ending message that says the program has
    finished running and also prints the number of calculations that have been
    made.
    num_calculation - the number of calculations the program has made"""
    print("")
    for number in range(3, 0, -1):
        print(number, "...", sep='')
    print("The program has finished running!")
    if num_calculation > 1:
        print("It made", num_calculation, "calculations.")
    else:
        print("It made 1 calculation.")


def do_addition(num1, num2, num_type):
    """The function adds two numbers and returns the sum as a floating point
    number or an integer depending on the type of input the user selected.
    num1 - an integer or floating point number, the first one inputted
    num2 - an integer or floating point number, the second one inputted
    num_type - the type of number that will be used, can be any value"""
    if num_type == "1":
        return int(num1 + num2)
    else:
        return float(num1 + num2)


def do_subtraction(num1, num2, num_type):
    """The function adds two numbers and returns the difference as a
    floating point number or an integer depending on the type of input the
    user selected.
    num1 - an integer or floating point number, the first one inputted
    num2 - an integer or floating point number, the second one inputted
    num_type - the type of number that will be used, can be any value"""
    if num_type == "1":
        return int(num1 - num2)
    else:
        return float(num1 - num2)


def do_multiplication(num1, num2, num_type):
    """The function multiplies two numbers and returns the product as a
    floating point number or an integer depending on the type of input the
    user selected as well as if the inputs are the same.
    num1 - an integer or floating point number, the first one inputted
    num2 - an integer or floating point number, the second one inputted
    num_type - the type of number that will be used, can be any value"""
    if num_type == "1" or (num1 * num2) % 1 == 0:
        return int(num1 * num2)
    else:
        return float(num1 * num2)


def do_division(num1, num2):
    """The function divides two numbers and returns the quotient as a floating
    point number or an integer depending on whether they divide evenly.
    num1 - an integer or floating point number, the first one inputted
    num2 - an integer or floating point number, the second one inputted"""
    if num1 % num2 == 0:
        return int(num1 / num2)
    else:
        return float(num1 / num2)


def do_exponentiation(num1, num2, num_type):
    """The function raises one number to the power of another and returns the
    result as a floating point number or an integer depending on the type of
    input the user selected.
    num1 - an integer or floating point number, the first one inputted
    num2 - an integer or floating point number, the second one inputted
    num_type - the type of number that will be used, can be any value"""
    if num_type == "1":
        return int(num1 ** num2)
    else:
        return float(num1 ** num2)


def do_modular_division(num1, num2, num_type):
    """The function divides two numbers and returns the remainder as a
    floating point number or an integer depending on the type of input the
    user selected.
    num1 - an integer or floating point number, the first one inputted
    num2 - an integer or floating point number, the second one inputted
    num_type - the type of number that will be used, can be any value"""
    if num_type == "1":
        return int(num1 % num2)
    else:
        return float(num1 % num2)


def test_integer(num):
    """The function tests whether the inputted number is an integer,
    preventing any errors that would crash the program.
    num - any type of input, meant to be an integer"""
    try:
        # https://www.geeksforgeeks.org/string-endswith-python/
        # The endswith prevents the rare error where a number ending with
        # a period passes through the conditional and crashes the program.
        if int(float(num)) == float(num) and not (num.endswith('.')):
            return True
    except ValueError:
        return False


def test_float(num):
    """The function tests whether the inputted number is a floating point
    number or an integer, preventing any errors that would crash the program.
    num - any type of input, meant to be a floating point number or integer"""
    try:
        if float(num):
            return True
    except ValueError:
        return False


def main():
    """The function acts as a calculator, taking two numbers and performing
    one of many operations on them to obtain and return a result. It can be
    repeated multiple times until the user chooses otherwise."""
    print_welcome()
    num_calculation = 0
    keep_running = "yes"
    while keep_running == "yes":
        number_type = input("\nEnter 1 if you would only like to use "
                            "integers or enter \nanything else if you would "
                            "like to use decimals as well: ")
        # The variable is used in a conditional statement to determine if the
        # printed statement at the end will include decimals.
        if number_type == "1":
            first_number = input("\nChoose your first number: ")
            # The while loop prevents the program from crashing.
            # while test_integer(first_number) != True:  # This is another,
            # less simple way to write it.
            while not test_integer(first_number):
                first_number = input("The number entered is not valid. "
                                     "Please enter an integer: ")
            first_number = int(first_number)
            second_number = input("\nChoose your second number: ")
            while not test_integer(second_number):
                second_number = input("The number entered is not valid. "
                                      "Please enter an integer: ")
            second_number = int(second_number)
        else:
            first_number = input("\nChoose your first number: ")
            while not test_float(first_number):
                first_number = input("The number entered is not valid. "
                                     "Please enter an integer/floating "
                                     "point number: ")
            first_number = float(first_number)
            second_number = input("\nChoose your second number: ")
            while not test_float(second_number):
                second_number = input("The number entered is not valid. "
                                      "Please enter an integer/floating "
                                      "point number: ")
            second_number = float(second_number)

        operation_list = ["+", "-", "*", "/", "**", "%", "//"]
        operation = input("\nChoose the operation you want to perform "
                          "(enter the symbol/operator): ")
        # This while loop ensures the inputted operation is in the preset list
        # of operations to prevent an error that could crash the program.
        while operation not in operation_list:
            print("Error! " * 3)
            print("The operation entered is not valid.")
            print("The valid operators are +, -, *, /, **, %, and //.")
            operation = input("Please choose the corresponding operator for "
                              "the operation you want to perform: ")
        # This checks if the operation is addition, then calculates the total.
        # It also uses the number_type variable to make the answer int/float.
        # The other parts of the conditional do the same for the corresponding
        # operation.
        if operation == "+":
            answer = do_addition(first_number, second_number, number_type)
        elif operation == "-":
            answer = do_subtraction(first_number, second_number, number_type)
        elif operation == "*":
            answer = do_multiplication(first_number, second_number,
                                       number_type)
        elif operation == "/":
            answer = do_division(first_number, second_number)
        elif operation == "**":
            answer = do_exponentiation(first_number, second_number,
                                       number_type)
        elif operation == "%":
            answer = do_modular_division(first_number, second_number,
                                         number_type)
        # The number_type variable has no effect on the result of floor
        # division (since it is always an integer), so it is not used to find
        # the answer.
        else:
            answer = int(first_number // second_number)

        print("")
        print(first_number, operation, second_number, "=", answer)
        print("The " + "answer is ", answer, ".", sep='', end='')
        num_calculation += 1
        keep_running = input("\n\nWould you like to continue running "
                             "the program? If so, enter 'yes'. \nOtherwise, "
                             "enter anything else: ")
    print_ending(num_calculation)


main()
