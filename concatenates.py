#!/usr/bin/env python3

# Created by: Lily Liu
# Created on: Oct 2021
# This program concatenates


def concatenate(first_things, second_things):
    # this function concatenate two lists
    concatenated_list = []

    # process
    for element in first_things:
        concatenated_list.append(element)

    for element in second_things:
        concatenated_list.append(element)

    return concatenated_list


def main():
    concatenated_list = []

    # input
    user_first_things = input("Enter the things to put in first list (no spaces): ")
    user_second_things = input("Enter the things to put in second list (no spaces): ")

    # output
    print("")
    concatenated_list = concatenate(user_first_things, user_second_things)

    print("The concatenated list is {0} ".format(concatenated_list))

    print("")
    print("Done.")


if __name__ == "__main__":
    main()
