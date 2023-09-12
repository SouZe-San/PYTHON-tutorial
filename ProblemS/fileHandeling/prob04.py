
#! problem no.4 the count the number of the line present in file

f = open('file01.txt')
lineList = f.readlines()
lineNo = len(lineList)
print(f"the Number of the Line in the File : {lineNo}")
print("Print odd Numbers line and index start from 0")
for i in range(lineNo):
    if (i%2 != 0):
        print(lineList[i])
f.close()