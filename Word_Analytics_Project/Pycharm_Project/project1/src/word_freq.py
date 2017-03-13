from helper import *
"""
Benjamin Mitchell
242-csapx
10/19/2016

Calculating the popularity of each word
"""

def sortByNumbers(dict):
    """
    Sorting the dictionary into a set of tuples

    :param dict: the dictionary of the word data
    :return: a set of tuples containing the same data, but sorted
    """
    temp = {}
    #Adding each piece of word data to a new dictionary
    for key in dict:
        temp[key] = dict[key].getNumber()
    #Returning the sorted set of tuples
    return list(reversed(sorted(temp.items(), key=operator.itemgetter(1))))

def find(wordDict, word, filename):
    """
    Finding the rank of the word within the (sorted) wordDict

    :param wordDict: set of Tuples containing word data (sorted)
    :param word: selected word
    :param filename: filename
    :return: returns the placement (rank) of the selected word
    """
    num = 0
    #If the word was found yet
    isFound = False
    #Check all entries in the data set
    for e in wordDict:
        num += 1
        #Return away from this for loop when the word is found
        if e[0] == word:
            isFound = True
            return num
    #Error out when the word was never found in the data set
    if not isFound:
        sys.stderr.write("Error: Word " + word + " does not appear in " + filename)
        exit()

def plotWords(wordDict, word, placement, filename):
    """
    Plotting the word_freq data

    :param wordDict: Set of Tuples containing word data
    :param word: the selected word
    :param placement: the position (rank) of the word
    :param filename: filename
    :return: none
    """
    x = []
    y = []
    num = 1

    #Creating the axis x, y sets of data for our graph
    for item in wordDict:
        y.append(int(item[1]))
        x.append(num)
        num += 1

    plt.title("Word Frequencies of: " + str(filename))
    plt.ylabel("Total number of occurrences")
    plt.xlabel("Rank of word " + "(\"" + word + "\" is rank " + str(placement) + ")")
    #Turns off bottom labels
    plt.tick_params(labelbottom='off')
    #Plots the points at which the data occurs
    plt.loglog(x, y, 'o', basex=10, basey=10, ms=4)
    #Plots a line connecting these points
    plt.loglog(x, y, basex=10, basey=10)
    #Placing the star
    plt.plot(int(placement), y[(int(placement)-1)], '*', ms=15)
    #Placing text
    plt.text(int(placement), y[(int(placement)-1)], word)
    #Controlling the scaling of the plot
    subplot = plt.subplot()
    subplot.autoscale_view(True, True, True)
    plt.show()

def main():
    """
    Main

    :return: None
    """
    # Reading the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output word frequencies to standard output.", type=int)
    parser.add_argument("-p", "--plot", help="Plot word frequencies using matplotlib", action="store_true")
    parser.add_argument("word", help="word")
    parser.add_argument("filename", help="A comma separated value unigram file")
    args = parser.parse_args()

    #Creating my helper object that contains re-used functions among my four programs
    helper = Helper()

    # Tests if the filename argument is an actual file
    helper.testFile(args.filename)
    #Gathers the data from the file, then sorts it into a set of tuples
    wordDict = sortByNumbers(helper.getDict(args.filename))
    #Finding the placement (rank) of the selected word
    placement = find(wordDict, args.word, args.filename)

    #Do standard output if selected
    if args.output is not None:
        helper.printSelection(wordDict, "wordFreq", args.word, args.output, placement)
    #Do plotting if selected
    if args.plot:
        plotWords(wordDict, str(args.word), placement, str(args.filename))


if __name__ == '__main__':
    main()