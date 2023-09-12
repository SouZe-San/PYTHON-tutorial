
# ! The First prob -> Copy the file content and write it into a another in UpperCase

f = open('file01.txt')
content = f.read()
print(content)
newLine = content.upper() # transform into Upper case the content of the other file
f.close()

f= open('copyFile.txt', 'w')
f.write(newLine)
f.close()
print("\n-----Now check both files manually----")