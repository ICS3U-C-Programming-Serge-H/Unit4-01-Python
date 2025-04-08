#!/usr/bin/env python3
# Created by: Serge Hamouche
# Created on: Mar 28, 2025
# This program will calculate the sum of the number the user inputs using loop.


def main():
    # This function uses a while loop
    loop_counter = 0
    total_sum = 0

    # Get user_number
    while True:
        try:
            positive_integer_str = input("Enter a positive integer: ")
            positive_integer = int(positive_integer_str)
            if positive_integer >= 0:
                break
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
                print("Invalid input. Please enter an integer.")
        print("")

    # process
    while loop_counter <= positive_integer:
        total_sum = total_sum + loop_counter
        loop_counter = loop_counter + 1

    print(f"The sum of numbers from 0 to {positive_integer} is: {total_sum}")


if __name__ == "__main__":
    main()
