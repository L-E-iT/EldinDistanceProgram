import math
import sys

print("=======================================================\n"
      "Welcome to the Eldin Nation Distance Program.\n"
      "Please follow the prompts and enter the coordinates\n"
      "with a space separating the X and Z coordinates\n"
      "Ex: 3457 -980\n"
      "=======================================================\n")


def main():
    first = str(input("What are the first town hall coordinates? ")).split()
    second = str(input("What are the second town hall coordinates? ")).split()
    xdist = int(first[0]) - int(second[0])
    zdist = int(first[1]) - int(second[1])
    distance = pythagorean(xdist, zdist)
    print("The distance between the two towns is:", distance)
    finish()


def pythagorean(xdist, zdist):
    return math.sqrt((xdist**2)+(zdist**2))


def finish():
    test = True
    print("=======================================================\n"
          "Thanks for using the program.\n"
          "if you would like to run it again, please enter 'Yes' below.\n"
          "if not, enter 'No'\n"
          "=======================================================\n")
    while test:
        choice = input("Yes/No: ")
        if choice.lower() == 'yes':
            main()
        elif choice.lower() =='no':
            sys.exit(1)
        else:
            print("Not valid input")


main()


