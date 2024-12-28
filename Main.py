import AmazonTests as at
import numpy as np
import pandas as pd
import datetime as dt


def main():
    # vars
    mynums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    print(" ********** Starting Tests ********** ")
    # Requirement: * DONE - Find out the longest non-repeatable charcters sub-string from string: str = "sudbamdquaxl"
    at.amazonTest1()

    # Requirement: * DONE - Find the highest sub string lenght in given string without repeating charcters. Str = "abhedabaik"
    at.amazonTest2()

    # Requirement: * DONE - Define a function that takes an array of numbers and returns an array of numbers of the same length.
    arrayResult = at.amazonTest3(mynums)
    print(arrayResult)

    # Requirement: * IN PROGRESS, Stacks
    at.amazonTest4()


if __name__ == "__main__":
    main()