from helper import *
"""
Benjamin Mitchell
242-csapx
10/19/2016

Calculating the number of times a chosen word appears in the file
"""

def main():
    """
    Main

    :return: None
    """
    #Reading the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("word", help="a word to display the total occurences of")
    parser.add_argument("filename", help="A comma separated value unigram file")
    args = parser.parse_args()

    helper = Helper()

    #Tests if the filename argument is an actual file
    helper.testFile(args.filename)
    #Creates the dictionary of all the words in the file and the times they appear
    wordDict = helper.getDict(str(args.filename))
    #Printing the selected word from the arguments
    helper.printSelection(wordDict, "wordCount", args.word, None, None)

if __name__ == '__main__':
    main()