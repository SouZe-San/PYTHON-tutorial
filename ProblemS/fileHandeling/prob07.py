
# ! Store lines in a list

f = open('file01.txt')
content = f.read() # Store the Whole Content Of the File in this variable
lineLis = content.split('\n')  # Split the Whole content when \n Find
print(lineLis)
