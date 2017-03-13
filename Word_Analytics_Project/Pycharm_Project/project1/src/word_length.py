from helper import *
"""
Benjamin Mitchell
242-csapx
10/19/2016

Calculating the average length of words over a span of years
"""

def plotYears(dict, filename, start, end):
    """
    Plots the data

    :param dict: dictionary of information
    :param filename: filename
    :param start: starting year
    :param end: ending year
    :return: None
    """
    x = []
    y = []

    #Setting x to te years and y to the average length of words for that year
    for year in dict:
        x.append(int(year[0]))
        y.append(year[1])

    #title and labels
    plt.title("Average word lengths from " + start + " to " + end + ": " + str(filename))
    plt.ylabel("Average Word Length")
    plt.xlabel("Year")
    # Plots a line
    plt.plot(x, y)
    # Controlling the scaling of the plot
    subplot = plt.subplot()
    subplot.autoscale_view(True, True, True)
    plt.show()

def checkYearRange(start, end):
    """
    Checks valid year range

    :param start: starting year
    :param end: ending year
    :return: none
    """
    #Checks valid year range
    if(start > end):
        sys.stderr.write("Error: start year must be less than or equal to end year!")
        exit()
    else:
        return

def avgDict(filename, start, end):
    """
    Gathers the information from the file, places it into a dictionary

    :param filename: Filename
    :param start: Starting year
    :param end: Ending year
    :return: populated dictionary of information
    """
    allWords = {}

    # Making a dictionary with the years as keys and Entry objects as values
    for i in range(int(start), int(end) + 1):
        allWords[str(i)] = Entry(0, 0)
    with open(filename) as input:
        # Reading in from a csv file
        read = csv.reader(input, delimiter=',')
        for line in read:
            #Populating the dictionary with the neccesary values.
            if line[1].strip() in allWords:
                allWords[line[1].strip()].updateStrValue(int(line[2]))
                allWords[line[1].strip()].updateNumber(len(line[0]) * int(line[2]))
    return allWords

def sortedYears(wordDict):
    """
    Sorts the dictionary of information

    :param wordDict: passed in dictionary of years and values
    :return: new sorted dictionary
    """
    temp = {}
    #Sorts the passed in dictionary, entering the data into a temp dict
    for key in wordDict:
        temp[key] = (wordDict[key].getNumber() / wordDict[key].getStrValue())

    return sorted(temp.items(), key=operator.itemgetter(0))

def main():
    """
    Main

    :return:  None
    """
    # Reading the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output Average Word Length to standard output.", action="store_true")
    parser.add_argument("-p", "--plot", help="Plot Average Word Length using matplotlib", action="store_true")
    parser.add_argument("start", help="the starting year range")
    parser.add_argument("end", help="the ending year range")
    parser.add_argument("filename", help="A comma separated value unigram file")
    args = parser.parse_args()

    helper = Helper()

    # Tests if the filename argument is an actual file
    helper.testFile(args.filename)
    # Checking to see if the range of years is valid
    checkYearRange(args.start, args.end)
    # Populating the main dictionary
    wordDict = avgDict(args.filename, args.start, args.end)
    # Sorting the dictionary
    wordDict = sortedYears(wordDict)

    #If standard output is desired
    if args.output:
        helper.printSelection(wordDict, "wordLength", None, None, None)
    #If plotting is desired
    if args.plot:
        plotYears(wordDict, args.filename, args.start, args.end)


if __name__ == '__main__':
    main()