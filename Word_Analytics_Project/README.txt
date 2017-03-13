Python Project 1 of Fall Semester 2016-2017

Using unigram data from Google arranged in a .csv file of word counts during that year, I created from scatch each
of these 4 sections of the project.

word_count.py - Gathers the number of occurences a particular word was used over all entries in the file.
letter_freq.py - Calculates the frequency of each letter in every word over every year in the file.
word_length.py - Calculates the average word length from entered year X to entered year Y.
word_freq.py - Calculates the top X used words, ranks them, and finds the rank of your entered word.

WARNING: There are two datafiles included that are used a lot.  short.csv for testing/quick examples,
and all.csv for a good analysis of word/letter historicle usage.  all.csv is very large, and will take a few
seconds to completely run through.

===============================================Word_Count======================================================
word_count.py USAGE:
	$python3 <WORD> <FILENAME>

Where WORD is:
	Any word you would like to search for.

Where FILENAME is:
	The .csv file containing entries.

Example Run:
	$python3 word_count.py president data/all.csv
===============================================Letter_Freq======================================================
letter_freq.py USAGE:
	$python3 -o -p <FILENAME>

Where -o is:
	<Optional> Output letter frequencies to standard output.

Where -p is:
	<Optional> Plot letter frequencies using matplotlib

Where FILENAME is:
	The .csv file containing entries.

Example Run:
	$python3 letter_freq.py -o -p data/all.csv
===============================================Word_Length======================================================
word_length.py USAGE:
	$python3 -o -p <STARTYEAR> <ENDYEAR> <FILENAME>

Where -o is:
	<Optional> Output Average Word Length to standard output.

Where -p is:
	<Optional> Plot Average Word Length using matplotlib

Where STARTYEAR and ENDYEAR are:
	The start and end years you wish to search for lengths.  See Example Runs.

Where FILENAME is:
	The .csv file containing entries.

Example Run:
	$python3 word_length.py -o -p 1980 2008 data/all.csv
===============================================Word_Freq======================================================
word_freq.py USAGE:
	$python3 -o <INT> -p <WORD> <FILENAME>

Where -o is:
	<Optional> Output word frequencies to standard output.

Where INT is:
	The number of top ranked words you want to see displayed.  See Example Runs.
	Do not include without -o.

Where -p is:
	<Optional> Plot word frequencies using matplotlib

Where WORD is:
	Any word you would like to search for.

Where FILENAME is:
	The .csv file containing entries.

Example Run:
	$python3 -o 60 -p president data/all.csv