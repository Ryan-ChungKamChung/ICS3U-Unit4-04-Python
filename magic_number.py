#!/usr/bin/env python3

# Created by Ryan Chung Kam Chung
# Created in November 2020
# Final version of magic_number

import random


def main():
    # this function sees if the user inputed the magic number

    print("Guess the magic number (0-9)!")

    random_number = random.randint(0, 9)

    while True:
        # Input
        magic_number_string = input("Please enter your guess: ")

        # Process
        try:
            magic_number = int(magic_number_string)

            if magic_number == random_number:
                # Output
                print("Nice! Your answer is right!")
                break
            elif magic_number > random_number:
                # Output
                print("Oops! Your guess is too high!")
            else:
                # Output
                print("Oops! Your guess is too low!")

        except Exception:
            print("This isn't an integer")


if __name__ == "__main__":
    main()
