# Joshua Lopez
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
    print("\nHello! This is a simple calculator.")
    print("It can perform addition, subtraction, multiplication, division,"
          "\nexponentiation, modular division, and floor division.")


def print_ending():
    for number in range(3, 0, -1):
        print(number, "...", sep='')
    print("The program has finished running!")


def do_addition(num1, num2, num_type):
    if (num_type == "1"):
        return int(num1 + num2)
    else:
        return float(num1 + num2)


def do_subtraction(num1, num2, num_type):
    if (num_type == "1"):
        return int(num1 - num2)
    else:
        return float(num1 - num2)


def do_multiplication(num1, num2, num_type):
    if (num_type == "1" or (num1 * num2) % 1 == 0):
        return int(num1 * num2)
    else:
        return float(num1 * num2)


def do_division(num1, num2):
    if (num1 % num2 == 0):
        return int(num1 / num2)
    else:
        return float(num1 / num2)


def do_exponentiation(num1, num2, num_type):
    if (num_type == "1"):
        return int(num1 ** num2)
    else:
        return float(num1 ** num2)


def do_modular_division(num1, num2, num_type):
    if (num_type == "1"):
        return int(num1 % num2)
    else:
        return float(num1 % num2)


def test_integer(num):
    try:
        if (int(float(num)) == float(num) and not (num.endswith('.'))):
            # https://www.geeksforgeeks.org/string-endswith-python/
            # The endswith prevents the rare error where a number ending with
            # a period passes through the conditional and crashes the program.
            return True
    except:
        return False


def test_float(num):
    try:
        if (float(num)):
            return True
    except:
        return False


def main():
    number_type = input("\nEnter 1 if you would only like to use integers or "
                        "enter \nanything else if you would like to use "
                        "decimals as well: ")
    # The variable is used in a conditional statement to determine if the
    # printed statement at the end will include decimals.

    if (number_type == "1"):
        first_number = input("Choose your first number: ")
        while (test_integer(first_number) != True):
            first_number = input("The number entered is not valid. "
                                 "Please enter an integer: ")
        # This makes sure the inputted number is an integer using a try
        # and except block. It also prevents the program from crashing.
        first_number = int(first_number)
        second_number = input("Choose your second number: ")
        while (test_integer(second_number) != True):
            second_number = input("The number entered is not valid. "
                                  "Please enter an integer: ")
        second_number = int(second_number)
    else:
        first_number = input("Choose your first number: ")
        while (test_float(first_number) != True):
            first_number = input("The number entered is not valid. "
                                 "Please enter an integer/floating point: ")
        first_number = float(first_number)
        second_number = input("Choose your second number: ")
        while (test_float(second_number) != True):
            second_number = input("The number entered is not valid. "
                                  "Please enter an integer/floating point: ")
        second_number = float(second_number)

    operation = input("Choose the operation you want to perform: ")
    if (operation == "addition" or operation == "+"):
        operator = "+"
        answer = do_addition(first_number, second_number, number_type)
    # This checks if the operation is addition, then calculates the total
    # and assigns the + operator to the operator variable for later use.
    # It also uses the number_type variable to make the answer int/float.
    # The other parts of the conditional do the same for the corresponding
    # operation.
    elif (operation == "subtraction" or operation == "-"):
        operator = "-"
        answer = do_subtraction(first_number, second_number, number_type)
    elif (operation == "multiplication" or operation == "*"):
        operator = "*"
        answer = do_multiplication(first_number, second_number, number_type)
    elif (operation == "division" or operation == "/"):
        operator = "/"
        answer = do_division(first_number, second_number)
    elif (operation == "exponentiation" or operation == "**"):
        operator = "**"
        answer = do_exponentiation(first_number, second_number, number_type)
    elif (operation == "modular division" or operation == "%"):
        operator = "%"
        answer = do_modular_division(first_number, second_number, number_type)
    elif (operation == "floor division" or operation == "//"):
        operator = "//"
        answer = int(first_number // second_number)
    else:
        print("\nError!" * 3, "\nThe operation entered is not valid.")
        print("Please enter the full name or its corresponding operator.")

    print(first_number, operator, second_number, "=", answer)
    print("The " + "answer is ", answer, ".", sep='', end='')


num_calculation = 0
keep_running = "yes"
while (keep_running == "yes"):
    print_welcome()
    main()
    num_calculation += 1
    keep_running = input("\n\nWould you like to continue running "
                         "the program? ")
# The while loop determines either loops the program or terminates it.
print_ending()
if (num_calculation > 1):
    print("It made", num_calculation, "calculations.")
else:
    print("It made 1 calculation.")
