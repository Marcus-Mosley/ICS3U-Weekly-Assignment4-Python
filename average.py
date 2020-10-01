#!/usr/bin/env python3

# Created by Marcus A. Mosley
# Created on September 2020
# This program finds the average of three integers,
#     only if they are between 0-100 inclusive


def main():
    # This function finds the average of three integers,
    #     only if they are between 0-100 inclusive

    # Input
    string_1 = input("Enter a number between 0 and 100 inclusive: ")
    string_2 = input("Enter a second number between 0 and 100 inclusive: ")
    string_3 = input("Enter a third number between 0 and 100 inclusive: ")
    print("")

    # Process & Output
    try:
        integer_1 = int(string_1)
        integer_2 = int(string_2)
        integer_3 = int(string_3)
    except Exception:
        print("You have not inputted three integers, please input three"
              " numbers between 0 and 100!")
    else:
        if integer_1 >= 0 and integer_1 <= 100:
            if integer_2 >= 0 and integer_2 <= 100:
                if integer_3 >= 0 and integer_3 <= 100:
                    average = (integer_1 + integer_2 + integer_3) / 3
                    print("The average of the numbers {0}, {1}, and {2} is"
                          " {3}!"
                          .format(integer_1, integer_2, integer_3, average))
                else:
                    print("I am so sorry, but I cannot average numbers more"
                          " than 100 or less than 0!")
            else:
                print("I am so sorry, but I cannot average numbers more than"
                      " 100 or less than 0!")
        else:
            print("I am so sorry, but I cannot average numbers more than 100"
                  " or less than 0!")


if __name__ == "__main__":
    main()
