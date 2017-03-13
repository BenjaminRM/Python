import matplotlib.pyplot as plt
import numpy as np
import argparse
import sys
import os
import csv
from entry import *
import string
import operator
#THESE "UNUSED" IMPORTS ARE USED ELSEWHERE
"""
Benjamin Mitchell
242-csapx
10/19/2016

Used in assisting the main 4 files do tasks:

Testing file validity
Read in the .csv file and store in a dictionary
printing desired output
"""

class Helper(object):

    def __init__(self):
        pass

    def testFile(self, filename):
        """
        Checks to see if the file that the user wants to read from exists

        :param filename: filename
        :return: none
        """
        #Checks if the file exists
        if os.path.isfile(filename):
            return
        #Otherwise, errors out when the file is not found
        else:
            sys.stderr.write("Error: " + str(filename) + " does not exist!")
            exit()

    def getDict(self, filename):
        """
        Gives the user a dictionary of the inputed word data

        :param filename:  filename
        :return: a dictionary of words for keys, and Entry objects for values
        """

        allWords = {}

        with open(filename) as input:
            #Reading in from a csv file
            read = csv.reader(input, delimiter=',')
            for line in read:
                #if the word is already in the dictionary, update it's total
                if line[0] in allWords:
                    allWords[line[0]].updateNumber(int(line[2]))
                # Otherwise, make a new entry into the diction with the word, new entry object
                else:
                    allWords[line[0]] = Entry(line[0], int(line[2]))
        return allWords

    def printSelection(self, dict, printType, word, num1, num2):
        """
        Does all the standard output for the four different programs

        :param filename: filename
        :param dict: the set of the data for that program
        :param printType: specifying which section of this method to call
        :param word: selected word by the user, if any
        :param num1: varying in use between each program's output
        :param num2: varying in use between each program's output
        :return: none
        """
        #PRINT TYPES
        #"wordCount" - Standard output for word_count.py
        #"letterFreq" - Standard output for letter_freq.py
        #"wordFreq" - Standard output for word_freq.py
        #"wordLength" - Standard output for word_length.py
        if(printType == "wordCount"):
            #Prints if the word is found
            if word in dict:
                print(word + ": " + str(dict[word].getNumber()))
            #Errors out when the word is not found
            else:
                sys.stderr.write("Error: Word " + word + " does not appear in " + filename)
                exit()
        elif(printType == "letterFreq"):
            #Printing all the letter frequency data
            for entry in dict:
                print(entry[0] + ": " + str(entry[1]))
        elif (printType == "wordFreq"):
            #Prints the selected word + rank
            print(word + " is ranked #" + str(num2))
            #Prints the word frequency data requested
            for i in range(0, num1):
                print("#" + str(i+1) + ": " + dict[i][0] + " -> " + str(dict[i][1]))
        elif (printType == "wordLength"):
            for year in dict:
                print(year[0] + ": " + str(year[1]))






















