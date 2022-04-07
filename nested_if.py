#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


import constants


def main():
    # I calculate circumference
    int_year = 0

    # input
    string_year = input("Enter year: ")

    # process & output
    try:
        int_year = int(string_year)
        if int_year % 4 == 0:
            if int_year % 100 == 0:
                if int_year % 400 == 0:
                    print("Is a leap year")
                else:
                    print("Not a leap year")
            else:
                print("Is a leap year")
        else:
            print("Not a leap year")
    except Exception:
        print("Invalid Input")
    print("\nDone.")


if __name__ == "__main__":
    main()
