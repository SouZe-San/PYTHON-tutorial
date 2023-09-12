
# @ PROBLEM :  Scraping And Finding Ordered Words In A Dictionary using Python

# Scraping

#     Using the python library requests we will fetch the data from the given URL
#     Store the content fetched from the URL as a string
#     Decoding the content which is usually encoded on the web using UTF-8
#     Converting the long string of content into a list of words

# Finding the ordered words

#     Traversing the list of words
#     Pairwise comparison of the ASCII value of every adjacent character in each word
#     Storing a false result if a pair is unordered
#     Otherwise printing the ordered word


import requests

# Scrapes the words from the URL below and stores
# them in a list


def getWords():

  # Load the Url Where more than 2000 word placed
    url = "http://www.puzzlers.org/pub/wordlists/unixdict.txt"
    fetchData = requests.get(url)

    # extracts the content of the webpage
    wordList = fetchData.content

    # decodes the UTF-8 encoded text and splits the string to turn it into a list of words
    wordList = wordList.decode("utf-8").split()

    return wordList


# function to determine whether a word is ordered or not
def isOrdered():

    # fetching the wordList
    collection = getWords()
    print(collection)
    # since the first few of the elements of the
    # dictionary are numbers, getting rid of those
    # numbers by slicing off the first 17 elements
    collection = collection[16:]
    word = ''

    for word in collection:
        result = 'Word is ordered'
        i = 0
        l = len(word) - 1

        if (len(word) < 3):  # skips the 1 and 2 lettered strings
            continue

        # traverses through all characters of the word in pairs
        while i < l:
            if (ord(word[i]) > ord(word[i+1])):
                result = 'Word is not ordered'
                break
            else:
                i += 1

        # only printing the ordered words
        if (result == 'Word is ordered'):
            print(word, ': ', result)


# execute isOrdered() function
if __name__ == '__main__':
    isOrdered()
