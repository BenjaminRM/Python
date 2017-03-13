from helper import *
"""
Benjamin Mitchell
242-csapx
10/19/2016

Calculating the frequency distribution of individual letters throughout the entire file
"""

def letterCount(dict):
    """
    Making a dictionary with each letter as a key

    :param dict: dictionary containing the .csv file information
    :return: a dictionary containing each letter and it's frequency
    """
    # Making a new dictionary to store each letter's information in
    letters = dict.fromkeys(string.ascii_lowercase, 0)
    total = 0

    # Populating the letters-totals dictionary
    for key in dict:
        for letter in key:
            letters[letter] += dict[key].getNumber()
            # Total to keep track of all letters
            total += dict[key].getNumber()

    # Changing the letter-total data to letter-frequency data
    for entry in letters:
        letters[entry] = letters[entry] / total

    return letters

def plotLetters(letters, filename):
    """
    Plotting the information

    :param letters: set of sorted letters and their frequencies
    :param filename: filename
    :return: None
    """
    x = []
    y = []

    # Making x a set of each char in the alphabet
    for c in string.ascii_lowercase:
        x.append(c)
    # Making y the set of their frequencies
    for n in letters:
        y.append(n[1])

    # Plotting setup and execution
    pos = np.arange(len(x))
    width = 1.0
    ax = plt.axes()
    ax.set_xticks(pos + (width / 2))
    ax.set_xticklabels(x)
    plt.bar(pos, y, width, color='r')
    plt.title("Letter Frequencies: " + filename)
    plt.ylabel("Frequency")
    plt.xlabel("Letter")
    plt.show()

def main():
    """
    Main

    :return: None
    """
    # Reading the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--output", help="Output letter frequencies to standard output.", action="store_true")
    parser.add_argument("-p", "--plot", help="Plot letter frequencies using matplotlib", action="store_true")
    parser.add_argument("filename", help="A comma separated value unigram file")
    args = parser.parse_args()

    helper = Helper()

    # Tests if the filename argument is an actual file
    helper.testFile(args.filename)
    # Creates the dictionary of all the words in the file and the times they appear
    wordDict = helper.getDict(args.filename)
    # Creates a set of tuples, and gathers the total number of letters in the file
    letterDict = letterCount(wordDict)
    # Sorts the set of tuples from A-Z
    letterDict = sorted(letterDict.items(), key=operator.itemgetter(0))

    # Do if output is selected
    if args.output:
        helper.printSelection(letterDict, "letterFreq", None, None, None)
    # Do if plotting is selected
    if args.plot:
        plotLetters(letterDict, str(args.filename))

if __name__ == '__main__':
    main()