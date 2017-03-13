"""
CSapx Lab 3: Tripods

A program that reads a file of N x M size, and determines the best positions for X
number of tripods.  Each 'best' position will be determined by the sum of 3 sides.


Author: Benjamin Mitchell | RIT CS
CSCI 242-04
"""
import collections
import sys
import rit_sort

#Creating the named tuple for ALL tripod possibilities
Tripods = collections.namedtuple("Tripods", "location, orientation, sum")

def print_placements(tripods, num):
    """
    Printing the best tripods, and removing the positions(locations) that are already taken

    :param tripods: List of sorted tripods from largest sum to smallest
    :param num: Number of desired placed tripods
    :return: none
    """
    print("Optimal placement: ")
    sum = 0
    #Looping for num of times, num being how many tripods will be placed
    for i in range(0, num):
        #total of all selected tripod's sums
        sum += tripods[0].sum
        print("Loc: " + str(tripods[0].location) + ", facing: " + tripods[0].orientation + ", sum: " + str(tripods[0].sum))
        #Removing all other possible tripods with the same location coordinates
        loc = tripods[0].location
        for tripod in list(tripods):
            if tripod.location == loc:
                tripods.remove(tripod)
    print("Total: " + str(sum))

def add_tripod(x, i, orientation, grid):
    """
    (Helper function for populate() )Function used to determine which surrounding integer values need to be added up
    based on the orientation of the tripod.

    :param x: Row position
    :param i: Column position
    :param orientation: direction the tripod is facing
    :param grid: the full grid from the file (Lists)
    :return: An entry into the named tuple
    """
    #Each case for different orientations
    if(orientation == "N"):
        #selects three surrounding integers to add up based on it's orientation
        sum = grid[x][i-1] + grid[x][i+1] + grid[x-1][i]
        return Tripods([x, i], orientation, sum)
    elif (orientation == "S"):
        sum = grid[x][i-1] + grid[x][i+1] + grid[x+1][i]
        return Tripods([x, i], orientation, sum)
    elif (orientation == "E"):
        sum = grid[x+1][i] + grid[x-1][i] + grid[x][i+1]
        return Tripods([x, i], orientation, sum)
    elif (orientation == "W"):
        sum = grid[x+1][i] + grid[x-1][i] + grid[x][i-1]
        return Tripods([x, i], orientation, sum)

def populate(masterList):
    """
    A general function for determining which positions on the grid should have which direction
    facing tripods.  Top row case, bottom row case, all rows in between, corners and edges.

    :param masterList: The 2-D list of lists representing the grid
    :return: populated list of named tuple objects of all possible tripod positions
    """
    fullList = []
    #For every row in the masterlist
    for x in range(0, len(masterList)):
        #For every integer in every row
        for i in range(0, len(masterList[x])):
            #If the number is in the first row, and is not a corner
            if (masterList[x] == masterList[0] and i != 0 and i != (len(masterList[x]) - 1)):
                fullList.append(add_tripod(x, i, "S", masterList))
            #If the number is in the bottom row, and is not a corner
            elif (masterList[x] == masterList[(len(masterList) - 1)] and i != 0 and i != (len(masterList[x]) - 1)):
                fullList.append(add_tripod(x, i, "N", masterList))
            #If the number is in any middle row
            elif (masterList.index(masterList[x]) > 0 and masterList.index(masterList[x]) < (len(masterList) - 1)):
                #If the number is on the left side of the grid
                if (i == 0):
                    fullList.append(add_tripod(x, i, "E", masterList))
                #If the number is on the right side of the grid
                elif (i == len(masterList[x]) - 1):
                    fullList.append(add_tripod(x, i, "W", masterList))
                #All other middle numbers (4 possible positions each)
                else:
                    fullList.append(add_tripod(x, i, "N", masterList))
                    fullList.append(add_tripod(x, i, "S", masterList))
                    fullList.append(add_tripod(x, i, "E", masterList))
                    fullList.append(add_tripod(x, i, "W", masterList))
    return fullList

def check_num_tripods(masterList, numOfTripods):
    """
    Checks entered number of desired tripods vs total possible tripods.

    :param masterList: The 2-D list of lists representing the grid
    :param numOfTripods: Number of desired placed tripods
    :return: none
    """
    #Total possible tripod placements (rows * columns - 4 corners)
    total = ((len(masterList) * len(masterList[0])) - 4)
    if(numOfTripods > total):
        print("Too many tripods to place!")
        exit()

def print_grid(masterList):
    """
    Prints the 2-D list of lists to look like the input file.  Easy visualization

    :param masterList: The 2-D list of lists representing the grid
    :return: none
    """
    #Simply prints the 2-D list of lists
    print("Master Grid List:")
    print(masterList)
    #Prints the list in grid form (as in the input file)
    print("Master Grid:")
    for row in masterList:
        print(" ".join(str(num) for num in row))

def create_grid(filename):
    """
    Uses the filename argument (from command line) to create the 2-D list of Lists representing the grid

    :param filename: filename argument from the command line
    :return: returns the 2-D list of lists representing the grid
    """
    gridList = []
    #For every line in the file, add it to the list (and every int into another inner-list)
    for line in open(filename):
        line.strip()
        row = [int(val) for val in line.split()]
        gridList.append(row)
    return gridList

def check_file():
    """
    Reads the filename argument from the command line

    :return: the name of the file the grid is stored in
    """
    filename = ""
    #If the correct arguments are given, assign filename
    if (len(sys.argv) == 2):
        filename = str(sys.argv[1])
    else:
        print("Usage: python3 tripods.py filename")
        exit()
    return filename

def main():
    """
    The main function

    :return: none
    """
    #Creates the grid if the check_file call returns
    masterList = create_grid(check_file())

    #Prints the list and grid
    print_grid(masterList)

    #Takes the input of desired tripods to be placed
    numOfTripods = int(input("Enter number of tripods: "))

    #Checks if the number entered above is a do-able number
    check_num_tripods(masterList, numOfTripods)

    #Sorts the list of namedtuples after it has been created
    tripodList = rit_sort.quick_sort(populate(masterList))

    #Prints the best possible tripod placements
    print_placements(tripodList, numOfTripods)

if __name__ == '__main__':
    main()