import pandas as pd
import numpy as np
import datetime




def codingExercise():
    print('coding exercise test')








def amazonTest1():
    # Requirement: * DONE - Find out the longest non-repeatable charcters sub-string from string: str = "sudbamdquaxl"

    print("***** TEST 1 *****")
    # create a dict for the alphabet
    mydict = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
        'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
        'w': 0, 'x': 0, 'y': 0, 'z': 0
    }

    # looking for duplicates
    test_string = ("abcDEFGHijklAmnoP".lower())

    print(mydict)

    # print the string by indexing its characters
    count = 0
    mysubstring = ''
    for x in test_string:
        # convert to lower
        mychar: str = test_string[count]

        # if a repeat is found
        if (mydict[mychar] == 1):
            break;

        mysubstring += mychar

        # dictionary updates need to use a list
        mydict.update({mychar: 1})
        count += 1

    print(mysubstring)


def amazonTest2():
    # Requirement: * DONE - Find the highest sub string lenght in given string without repeating charcters. Str = "abhedabaik"

    print("***** TEST 2 *****")

    # create a dict for the alphabet
    mydict2 = {
        'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 'j': 0, 'k': 0,
        'l': 0, 'm': 0, 'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0,
        'w': 0, 'x': 0, 'y': 0, 'z': 0
    }

    # looking for duplicates
    test_string = ("abhedabaik".lower())

    print(mydict2)

    # print the string by indexing its characters
    count = 0
    mysubstring = ''
    for x in test_string:
        # convert to lower
        mychar: str = test_string[count]

        # if a repeat is found
        if (mydict2[mychar] == 1):
            break;

        mysubstring += mychar

        # dictionary updates need to use a
        mydict2.update({mychar: 1})
        count += 1

    print(mysubstring)
    print("Length of the substring is: " + str(len(mysubstring)))


def amazonTest3(numarray):
    # Requirement: * DONE - Define a function that takes an array of numbers and returns an array of numbers of the same length.

    print("***** TEST 3 *****")
    for i in range(len(numarray)):
        print(numarray[i])
        numarray[i] = int(numarray[i] + 100)
    return numarray


def amazonTest4():
    # Requirement: * Date and time, data types, stacks, list.

    print("***** TEST 4 (Stacks) *****")
    stack = []

    # Append/push elements to the stack
    stack.append('a')
    stack.append('b')
    stack.append('c')

    print('Initial stack')
    print(stack)

    # Pop elements off hte stack LIFO
    print('\nElements popped from stack:')
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

    print('\nStack after elements are popped:')
    print(stack)

    print("***** TEST 5 (datetime) *****")
    mydt = datetime.datetime.now()
    print(mydt)
    print(mydt.year)
    print(mydt.month)
    print(mydt.day)
    print(mydt.strftime("%A"))

    x = datetime.datetime(2018, 6, 1)

    print(x.strftime("%A"))
    print(x.strftime("%B"))
    #print(x.strftime("%C"))
    print(x.strftime("%D"))
    #print(x.strftime("%E"))
    print(x.strftime("%F"))
