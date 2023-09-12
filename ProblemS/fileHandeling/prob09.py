# ! Find the Most frequently used

def freWords(wordList):
    count = 1
    word = "No One"
    for i in wordList:
        current_word_Count = wordList.count(i)
        if (current_word_Count > count):
            count = current_word_Count
            word = i
    return word     

f = open('file01.txt')
content = f.read() # Store the Whole Content Of the File in this variable
lineLis = content.split()  # Split the Whole content when \n Find
print(freWords(lineLis))
f.close()