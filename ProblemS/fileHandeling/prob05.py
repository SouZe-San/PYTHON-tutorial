
f = open('file01.txt')
lineList = f.readlines()
lineNo = len(lineList)
print(f"the Number of the Line in the File : {lineNo}")
lineNo = int(input("Enter Line Numbers index start from 1:: "))
print(lineList[lineNo])
f.close()